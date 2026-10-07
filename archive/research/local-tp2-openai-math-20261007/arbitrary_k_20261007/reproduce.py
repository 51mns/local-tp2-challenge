#!/usr/bin/env python3
"""Replay every new exact certificate in a clean temporary directory.

Only Python's standard library is required. Saved inputs are never
regenerated in place. The fixed manifest and all output byte hashes are
checked, including decompressed certificates. Inherited proof packages
are pinned in DEPENDENCIES.md and have their own prior replay records.
"""
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
import gzip,json,os,platform,shutil,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parent
PHASES=[
 [(['arbk_seed/verify_old_normalized_constants.py','--max-m','69'],'arbk_seed/old_normalized_constants.json'),
  (['arbk_seed/verify_seed_subtraction.py'],'arbk_seed/seed_subtraction_certificates.json'),
  (['arbk_mixed/m0_normalized_blocks.py','--residues'],'arbk_mixed/m0_normalized_blocks_results.json'),
  (['arbk_mixed/finite_m_normalized_blocks.py'],'arbk_mixed/finite_m_normalized_blocks_results.json'),
  (['arbk_mixed/finite_mixed_kernels.py'],'arbk_mixed/finite_mixed_kernels_results.json'),
  (['arbk_root/verify_finite_ray_bridge.py'],'arbk_root/finite_ray_bridge_results.json')],
 [(['arbk_root/verify_scalar_closure.py'],'arbk_root/scalar_closure_results.json'),
  (['arbk_mixed/audit_seed_bounds.py'],'arbk_mixed/seed_bounds_independent_audit.json'),
  (['arbk_seed/audit_normalized_blocks.py'],'arbk_seed/normalized_blocks_independent_audit.json'),
  (['arbk_root/audit_finite_mixed.py'],'arbk_root/finite_mixed_independent_results.json'),
  (['arbk_audit/audit_finite_ray_bridge.py'],'arbk_audit/finite_ray_bridge_independent_results.json')],
 [(['arbk_audit/audit_scalar_closure.py'],'arbk_audit/scalar_closure_independent_results.json')]
]

def digest(data):return sha256(data).hexdigest()
def utc():return datetime.now(timezone.utc).isoformat()

def main():
    started=utc();manifest=json.loads((ROOT/'FILE_MANIFEST.json').read_text())
    checks=[]
    for item in manifest['files']:
        p=ROOT/item['path'];raw=p.read_bytes() if p.is_file() else b''
        checks.append({'path':item['path'],'sha256':digest(raw),'matches':len(raw)==item['bytes'] and digest(raw)==item['sha256']})
    assert checks and all(r['matches'] for r in checks),'Fixed package integrity failed'
    compressed=json.loads((ROOT/'COMPRESSED_CERTIFICATES.json').read_text())['records']
    expected={}
    for phase in PHASES:
        for args,result in phase:
            p=ROOT/result
            if p.exists():expected[result]=digest(p.read_bytes())
    for item in compressed:
        raw=gzip.decompress((ROOT/item['gzip_path']).read_bytes())
        assert len(raw)==item['uncompressed_bytes'] and digest(raw)==item['uncompressed_sha256']
        expected[item['json_path']]=digest(raw)
    runs=[];failed=False
    with tempfile.TemporaryDirectory(prefix='tp2_three_run_') as directory:
        work=Path(directory)
        for item in manifest['files']:
            dest=work/item['path'];dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/item['path'],dest)
        for item in compressed:
            dest=work/item['json_path'];dest.write_bytes(gzip.decompress((work/item['gzip_path']).read_bytes()))
        def run(job):
            args,result=job;t=time.monotonic()
            env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
            try:
                done=subprocess.run([sys.executable]+args,cwd=work,env=env,capture_output=True,text=True,timeout=300)
                out,err,code=done.stdout,done.stderr,done.returncode
            except subprocess.TimeoutExpired as exc:
                out,err,code=str(exc.stdout or ''),str(exc.stderr or ''),124
            actual=digest((work/result).read_bytes()) if (work/result).exists() else None
            passed=code==0 and actual==expected.get(result)
            return {'command':['python3']+args,'exit_code':code,'elapsed_seconds':round(time.monotonic()-t,3),
                'result':result,'expected_sha256':expected.get(result),'regenerated_sha256':actual,
                'byte_hash_matches':actual==expected.get(result),'status':'PASS' if passed else 'FAIL',
                'stdout_sha256':digest(out.encode()),'stderr_sha256':digest(err.encode()),
                'stdout_tail':out[-2000:],'stderr_tail':err[-2000:]}
        for number,phase in enumerate(PHASES,1):
            with ThreadPoolExecutor(max_workers=3) as pool:
                futures=[pool.submit(run,job) for job in phase]
                for future in as_completed(futures):
                    rec=future.result();runs.append(rec)
                    print('phase',number,rec['command'][1],rec['status'],flush=True)
                    failed|=rec['status']!='PASS'
            if failed:break
    order={args[0]:i for i,(args,_) in enumerate(job for phase in PHASES for job in phase)}
    runs.sort(key=lambda rec:order[rec['command'][1]])
    after=all((ROOT/item['path']).is_file() and digest((ROOT/item['path']).read_bytes())==item['sha256'] for item in manifest['files'])
    passed=not failed and after and len(runs)==12
    result={'status':'PASS' if passed else 'FAIL','started_utc':started,'completed_utc':utc(),
        'scope':'12 new author/audit programs; all regenerated exact JSON byte hashes; inherited mathematical lemmas are pinned separately',
        'python':platform.python_version(),'implementation':platform.python_implementation(),
        'arithmetic':'Python integers and fractions.Fraction; exact continuum Bernstein certificates',
        'fixed_manifest_files':len(checks),'fixed_files_unchanged':after,'fixed_file_checks':checks,
        'program_count':len(runs),'matching_regenerated_results':sum(r['byte_hash_matches'] for r in runs),
        'runs':runs,'independence':'Separate methods/implementations in the same shared session; not blind/external or formal verification'}
    (ROOT/'REPLAY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['fixed_file_checks','runs']},indent=2),flush=True)
    return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
