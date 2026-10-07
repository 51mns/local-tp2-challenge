"""Merge disjoint independent audit segments and compare primary metadata.

The expected primary output is opened only after both independent segments are
complete and the exact case sequence 0..409 has been checked.  No primary code
is imported.  This finalizer does not perform or change mathematical arithmetic.
"""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    segments = [here/'finite_audit_prefix_results.json', here/'finite_audit_tail_results.json']
    rows = []
    execution = []
    for path, requested_scope in zip(segments, [[0, 349], [350, 409]]):
        raw = path.read_bytes()
        data = json.loads(raw)
        assert data['status'] == 'PASS'
        assert data['scope'] == data['scope_completed'] == requested_scope
        assert all(case['negative'] == case['zero'] == 0 for case in data['cases'])
        rows.extend(data['cases'])
        execution.append(dict(file=path.name, scope=requested_scope,
                              cases=len(data['cases']), elapsed_seconds=data['elapsed_seconds'],
                              file_sha256=sha256(raw).hexdigest()))
    keys = [(row['m'], row['smooth'], row['label']) for row in rows]
    exact_keys = [(m, smooth, label) for m in range(410)
                  for smooth in [False, True] for label in ['single', 'midpoint']]
    assert keys == exact_keys
    assert sum(row['margins'] for row in rows) == 14766150
    # First access to the primary expected results in this finalizer.
    primary_path = here/'kernels_certificate_results.json'
    primary_raw = primary_path.read_bytes()
    primary = json.loads(primary_raw)
    assert primary['status'] == 'PASS' and primary['scope'] == [0, 409]
    assert len(primary['cases']) == len(rows) == 1640
    matches = []
    for actual, expected in zip(rows, primary['cases']):
        for key in ['m', 'smooth', 'label', 'degree', 'margins', 'negative', 'zero',
                    'minimum', 'witness', 'sha256']:
            assert actual[key] == expected[key], (actual['m'], actual['smooth'], actual['label'], key)
        if actual['label'] == 'single':
            assert actual['lambda_numerator'] == expected['lambda_numerator']
            assert int(actual['lambda_denominator']) == expected['lambda_denominator']
            assert expected['scale'] == 4*int(actual['lambda_denominator'])
        else:
            assert actual['alpha'] == expected['alpha']
            assert actual['b0'] == expected['reference_central']
            assert expected['scale'] == 8
        matches.append(dict(m=actual['m'], smooth=actual['smooth'], label=actual['label'],
                            full_hash_match=True, metadata_match=True))
    first = json.loads(segments[0].read_text())
    result = {k:v for k,v in first.items()
              if k not in ['cases', 'scope', 'scope_completed', 'elapsed_seconds',
                           'strict_minimum', 'total_margins']}
    result.update(status='PASS', scope=[0, 409], scope_completed=[0, 409], cases=rows,
                  total_cases=len(rows), total_margins=sum(row['margins'] for row in rows),
                  strict_minimum=min((row['minimum'] for row in rows), key=int),
                  minima_by_label={label:min((row['minimum'] for row in rows if row['label']==label),key=int)
                                   for label in ['single', 'midpoint']},
                  margins_by_label={label:sum(row['margins'] for row in rows if row['label']==label)
                                    for label in ['single', 'midpoint']},
                  run_execution=dict(segments=execution, commands=[
                      'python finite_audit_independent.py --output finite_audit_independent_results.json (checkpoint reached 0..355; retained 0..349 and discarded completed overlap 350..355)',
                      'python finite_audit_independent.py --min 350 --max 409 --output finite_audit_tail_results.json'],
                      retained_scopes=[[0,349],[350,409]], prefix_original_checkpoint_scope=[0,355],
                      discarded_overlap_scope=[350,355],
                      original_script_sha256=sha256((here/'finite_audit_independent.py').read_bytes()).hexdigest(),
                      finalizer_sha256=sha256(Path(__file__).read_bytes()).hexdigest()),
                  writer_comparison=dict(status='PASS', matched_cases=len(matches),
                      primary_file=primary_path.name, primary_file_sha256=sha256(primary_raw).hexdigest(),
                      expected_opened_after_all_independent_cases_completed=True,
                      compared_fields=['m','smooth','label','degree','margins','negative','zero',
                          'minimum','witness','sha256','single lambda numerator/denominator and scale',
                          'midpoint alpha/reference central and scale'],
                      cases=matches))
    output = here/'finite_audit_independent_results.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','scope','total_cases','total_margins',
                                          'strict_minimum','minima_by_label','margins_by_label']},indent=2))
    print('All 1640 complete case hashes and metadata match the primary writer.')


if __name__ == '__main__':
    main()
