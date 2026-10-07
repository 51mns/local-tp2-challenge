#!/usr/bin/env python3
"""Replay exact identities and finite seeds; this does not prove closure.

Run from a checkout containing the read-only parent foundations.
The historical bounded off-Fricke scan is deliberately not expanded/repeated.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PAIRS = [
    ('center_character_reproducer.py', 'center_character_results.json'),
    ('gap_trace_reproducer.py', 'gap_trace_results.json'),
    ('gap_curvature_reproducer.py', 'gap_curvature_results.json'),
    ('multiplier_exact.py', 'multiplier_exact_results.json'),
    ('proxy_curvature_verify.py', 'proxy_curvature_results.json'),
    ('proxy_fricke_verify.py', 'proxy_fricke_results.json'),
    ('packet_transport_verify.py', 'packet_transport_results.json'),
    ('adversarial_packet_check.py', 'adversarial_packet_check_results.json'),
]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    runs = []
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    for script, result in PAIRS:
        expected = HERE.joinpath(result).read_bytes()
        proc = subprocess.run(
            [sys.executable, str(HERE / script)], cwd=HERE,
            env=env, capture_output=True, text=True, timeout=60,
        )
        if proc.returncode:
            raise RuntimeError(script + '\n' + proc.stdout + proc.stderr)
        actual = HERE.joinpath(result).read_bytes()
        assert actual == expected, ('saved result changed', result)
        if script == 'packet_transport_verify.py':
            assert json.loads(proc.stdout) == json.loads(expected)
        runs.append(dict(script=script, result=result, exit_code=0,
                         result_sha256=digest(actual)))
    for name in ('gap_manifest.json', 'multiplier_manifest.json'):
        manifest = json.loads(HERE.joinpath(name).read_text())
        entries = manifest.get('files_sha256', manifest.get('sha256'))
        assert isinstance(entries, dict), name
        for filename, expected_sha in entries.items():
            assert digest(HERE.joinpath(filename).read_bytes()) == expected_sha, filename
    report = dict(
        status='PASS', replays=runs,
        scope='Exact formal identities and finite seeds/obstacles only; analytical proofs are audited separately.',
        full_tree_Local_TP2='OPEN',
        remaining_analytic_obligation_families=[
            'Both-child current paired midpoint MP_2, including root edges',
            'Both-child strict proxy on regular expanded states',
        ],
        historical_bounded_scan='Not rerun; never used as an all-tree proof',
    )
    HERE.joinpath('replay_results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(status='PASS', exact_replays=len(runs), full_tree_Local_TP2='OPEN')))

if __name__ == '__main__':
    main()
