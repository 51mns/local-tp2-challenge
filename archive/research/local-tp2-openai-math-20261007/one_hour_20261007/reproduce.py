#!/usr/bin/env python3
"""Reproduce the complete finite certificate and independent audit package.

From this directory in the VS Code integrated terminal: python3 reproduce.py
Only Python's standard library is required. The infinite theorem additionally
depends on the written proof and the explicitly named prior foundation lemmas.
"""
from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import gzip
import json
import platform
import shutil
import subprocess
import sys
import tempfile
import time


ROOT=Path(__file__).resolve().parent
SCRIPTS=(
    'hour_invariant/verify_r2_ray.py',
    'hour_quantum/lrrl_certificate.py',
    'hour_quantum/uniform_ax_normalized.py',
    'hour_quantum/uniform_seed_strength.py',
    'hour_transport/verify_trace_transport.py',
    'hour_transport/verify_uniform_mixed_transport.py',
    'hour_root/verify_uniform_ray_closure.py',
    'hour_quantum/audit_r2_ray.py',
    'hour_invariant/audit_lrr_independent.py',
    'hour_quantum/audit_uniform_seed_finite.py',
    'hour_quantum/audit_all_m_transport.py',
    'hour_transport/audit_uniform_ray_closure.py',
    'hour_transport/explore_arbitrary_k_trace.py',
    'hour_invariant/audit_arbitrary_k_trace.py',
)


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    started=datetime.now(timezone.utc)
    manifest=json.loads((ROOT/'FILE_MANIFEST.json').read_text())
    integrity=[]
    for item in manifest['files']:
        p=ROOT/item['path']
        good=p.is_file() and digest(p)==item['sha256']
        integrity.append({'path':item['path'],'matches':good})
        if not good:
            raise AssertionError('Stored-file hash mismatch: '+item['path'])
    print('Stored-file integrity: PASS',flush=True)
    compressed=json.loads((ROOT/'COMPRESSED_CERTIFICATES.json').read_text())
    runs=[]
    regenerated=[]
    with tempfile.TemporaryDirectory(prefix='local_tp2_replay_') as location:
        work=Path(location)
        for name in ['hour_root','hour_quantum','hour_transport','hour_invariant']:
            shutil.copytree(ROOT/name,work/name)
        expected={}
        for item in compressed:
            raw=gzip.decompress((work/item['path']).read_bytes())
            assert len(raw)==item['unpacked_size']
            assert sha256(raw).hexdigest()==item['unpacked_sha256']
            p=work/item['unpacked_path']
            p.write_bytes(raw)
            expected[item['unpacked_path']]=item['unpacked_sha256']
        # Small archived JSON results are deterministic too. These include
        # the separate implementations' outputs and the scalar audit record.
        for name in ['hour_root','hour_quantum','hour_transport','hour_invariant']:
            for p in (work/name).glob('*.json'):
                expected.setdefault(str(p.relative_to(work)),digest(p))
        print('Complete certificate expansion: PASS',flush=True)
        for script in SCRIPTS:
            before=time.monotonic()
            result=subprocess.run([sys.executable,str(work/script)],cwd=work,
                                  capture_output=True,text=True,encoding='utf-8',timeout=300)
            record={'script':script,'exit_code':result.returncode,
                    'seconds':round(time.monotonic()-before,3),
                    'stdout':result.stdout,'stderr':result.stderr}
            runs.append(record)
            print(script+(': PASS' if result.returncode==0 else ': FAIL'),flush=True)
            if result.returncode:
                print(result.stderr,file=sys.stderr)
                break
        for relative,wanted in sorted(expected.items()):
            actual=digest(work/relative)
            regenerated.append({'path':relative,'expected_sha256':wanted,
                                'regenerated_sha256':actual,'matches':actual==wanted})
    passed=len(runs)==len(SCRIPTS) and all(r['exit_code']==0 for r in runs) and all(r['matches'] for r in regenerated)
    report={'status':'PASS' if passed else 'FAIL',
            'scope':'Finite exact certificates, separate reconstructions, and file integrity for the all-L^m-R^2-L^ell proof package; analytic theorem requires the written proof.',
            'started_utc':started.isoformat(),'finished_utc':datetime.now(timezone.utc).isoformat(),
            'python':platform.python_version(),'arithmetic':'Python int and fractions.Fraction',
            'stored_file_checks':integrity,'runs':runs,'regenerated_json_checks':regenerated,
            'independence':'Shared-session separate implementations and mathematical reviews; not blind, external, or formal verification.'}
    (ROOT/'REPLAY_RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    for item in regenerated:
        if not item['matches']:
            print('Regenerated hash mismatch:',item['path'],file=sys.stderr)
    print('Regenerated certificate hashes: '+('PASS' if all(r['matches'] for r in regenerated) else 'FAIL'),flush=True)
    print('Final finite-replay verdict: '+report['status'],flush=True)
    return 0 if passed else 1


if __name__=='__main__':
    raise SystemExit(main())
