#!/usr/bin/env python3
"""Replay bounded exact witnesses and check the fixed research source manifest.

Run from the research directory in the VS Code integrated terminal:
    python3 reproduce.py
Only the Python standard library is required. This is not a full-tree scan.
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    "verify_quantum_applicability.py",
    "verify_rayleigh_transfer.py",
    "independent_verify.py",
)


def verify_manifest():
    checks = []
    for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        expected, relative = line.split("  ", 1)
        target = ROOT / relative
        actual = hashlib.sha256(target.read_bytes()).hexdigest() if target.is_file() else None
        checks.append({"file": relative, "expected_sha256": expected,
                       "actual_sha256": actual, "matches": actual == expected})
    if not checks:
        raise ValueError("The fixed-source manifest is empty.")
    return checks


def main():
    hashes = verify_manifest()
    if not all(c["matches"] for c in hashes):
        for c in hashes:
            if not c["matches"]:
                print("HASH MISMATCH:", c["file"], file=sys.stderr)
        return 1

    log_dir = ROOT / "replay_logs"
    log_dir.mkdir(exist_ok=True)
    runs = []
    for script in SCRIPTS:
        result = subprocess.run(
            [sys.executable, str(ROOT / script)], cwd=ROOT,
            capture_output=True, text=True, encoding="utf-8", timeout=60,
        )
        name = Path(script).stem
        output = log_dir / (name + ".stdout.txt")
        errors = log_dir / (name + ".stderr.txt")
        output.write_text(result.stdout, encoding="utf-8")
        errors.write_text(result.stderr, encoding="utf-8")
        runs.append({"script": script, "exit_code": result.returncode,
                     "stdout": str(output.relative_to(ROOT)),
                     "stderr": str(errors.relative_to(ROOT))})
        print(script + ": " + ("PASS" if result.returncode == 0 else "FAIL"))

    hashes_after = verify_manifest()
    passed = all(r["exit_code"] == 0 for r in runs) and all(c["matches"] for c in hashes_after)
    report = {
        "status": "PASS" if passed else "FAIL",
        "scope": "Exact finite witnesses and fixed-file integrity; full Local TP2 remains OPEN",
        "utc_time": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "arithmetic": "Python integers and fractions.Fraction; no floating-point conclusions",
        "runs": runs,
        "fixed_source_hashes": hashes_after,
        "generated_result_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in ("rayleigh_transfer_results.json", "independent_results.json")
            if (ROOT / name).is_file()
        },
        "independence": "Separate implementation in the same session; not blind or external review",
    }
    (ROOT / "replay_results.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("Fixed source hashes:", "PASS" if all(c["matches"] for c in hashes_after) else "FAIL")
    print("Full Local TP2: OPEN")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
