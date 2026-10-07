"""Run exact identities and two separate constructions in an isolated folder.

Mac / VS Code integrated terminal, in this directory: python3 reproduce.py
Only the standard library is required. No network or persistent repo mutation.
"""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import json
import platform
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
SCRIPTS=('symbolic.py','author.py','verifier.py')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    fixed_checks={name:sha(ROOT/name)==digest for name,digest in manifest['fixed_sources'].items()}
    if not all(fixed_checks.values()):
        raise RuntimeError('Fixed source checksum mismatch')
    start=datetime.now(timezone.utc).isoformat()
    runs=[]
    output=ROOT/'certificates'
    output.mkdir(exist_ok=True)
    with TemporaryDirectory(prefix='tp2_fricke_') as tmp:
        temp=Path(tmp)
        for script in SCRIPTS:
            shutil.copy2(ROOT/script,temp/script)
        for script in SCRIPTS:
            before=time.monotonic()
            proc=subprocess.run([sys.executable,script],cwd=temp,capture_output=True,text=True,
                                encoding='utf-8',timeout=45)
            entry={'script':script,'exit_code':proc.returncode,
                   'elapsed_seconds':round(time.monotonic()-before,3),
                   'stdout':proc.stdout.strip(),'stderr':proc.stderr.strip()}
            runs.append(entry)
            if proc.returncode:
                raise RuntimeError(entry)
        author=temp/'author_results.json'
        verifier=temp/'verifier_results.json'
        if author.read_bytes()!=verifier.read_bytes():
            raise RuntimeError('Separate constructions disagree')
        data=json.loads(author.read_text())
        symbolic=json.loads((temp/'symbolic_results.json').read_text())
        for name in ('author_results.json','verifier_results.json','symbolic_results.json'):
            digest=sha(temp/name)
            expected=manifest['expected_results'].get(name)
            if digest!=expected:
                raise RuntimeError('Regenerated checksum mismatch: '+name)
            shutil.copy2(temp/name,output/name)
        report={
            'status':'PASS','started_utc':start,'completed_utc':datetime.now(timezone.utc).isoformat(),
            'python':platform.python_version(),'implementation':platform.python_implementation(),
            'arithmetic':'Python integers and fractions.Fraction; no floating-point proof conclusions',
            'base_commit':'0f7bb105a3330ba890528bb60b1f85ef6debcef5',
            'runs':runs,'fixed_sources_unchanged':all(sha(ROOT/n)==h for n,h in manifest['fixed_sources'].items()),
            'separate_output_bytes_identical':True,
            'identity_count':len(symbolic['identities']),
            'bounded_depth':data['depth'],'bounded_state_count':data['state_count'],
            'bounded_supported_minors':data['checked_supported_minors'],
            'bounded_negative_seed_checks':sum(len(r['negative_seed_bounds']) for r in data['records']),
            'regenerated_sha256':{n:sha(output/n) for n in manifest['expected_results']},
            'independence':'Separate algorithms by the same model; not blind, external or independent-model review.',
            'scope':'Written induction proves the algebraic statements. The bounded positive TP2 checks do not prove the full-tree target.',
            'mathematical_status':'PROOF_CANDIDATE; full-tree Local TP2 remains open'
        }
        (ROOT/'RUN_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Exact identities: PASS')
    print('Separate constructions and saved hashes: PASS')
    print('Full-tree Local TP2: OPEN')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
