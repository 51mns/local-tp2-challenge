"""Fast saved-evidence and integrity check; NOT an all-tree proof checker."""
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE / name).read_text())


def at(row, n):
    return row[abs(n)] if abs(n) < len(row) else 0


def defects(row):
    return [at(row,n)**2-at(row,n-1)*at(row,n+1)-at(row,n+1)**2
            +at(row,n)*at(row,n+2) for n in range(len(row))]


def minors(p, q):
    return [at(p,n)*at(q,n+1)-at(p,n+1)*at(q,n)
            for n in range(len(p))]


def check():
    frozen = read('falsification_manifest.json')
    for name, item in frozen['files'].items():
        data = (HERE / name).read_bytes()
        assert len(data) == item['bytes'], name
        assert sha256(data).hexdigest() == item['sha256'], name

    reduction = read('reduction_common_results.json')
    assert reduction['nodes'] == 63
    assert set(reduction['fails']) == {'lr_R_G', 'lr_E_G'}
    assert all(v == {'path':'','index':0,'value':-2}
               for v in reduction['fails'].values())

    audit = read('network_reduction_audit_results.json')
    for state in [audit['root'], *audit['children'].values()]:
        row, gates = state['rows'], state['gates']
        assert defects(row['G']) == gates['delta_G']
        assert defects(row['M']) == gates['delta_M']
        assert minors(row['Q'], row['Pi']) == gates['proxy_Q_Pi']
        assert minors(row['S'], row['D']) == state['target']
        assert all(v > 0 for values in gates.values() for v in values)
        assert all(v > 0 for v in state['target'])
    for child in audit['children'].values():
        assert all(v >= 0 for values in child['links'].values() for v in values)
        assert all(v >= 0 for values in child['endpoint_links'].values() for v in values)

    exterior = read('network_exterior_results.json')['right_child']
    assert exterior['all_canonical_det_one_and_skew_verified'] is True
    assert sum(exterior['central_category_sums'].values()) == 271
    assert exterior['tail_diagonal_obstruction']['contribution'] == -72
    for term in exterior['central_source_terms']:
        assert term['contribution'] == term['coefficient'] * term['weight']
    assert sum(t['contribution'] for t in exterior['central_source_terms']) == 271

    seeds = read('invariant_signed_seed_results.json')
    assert seeds['symbolic_checks'] == 9
    root = seeds['root_X_packet']
    assert defects(root['half_row']) == root['defects']
    assert root['defects'][0] == -388
    assert seeds['analytic_obstruction_plain_from_m'] == 6
    assert seeds['analytic_obstruction_smooth_from_m'] == 5
    assert 3**6 > Fraction(49,2)*(2*6+1)
    assert 3**5 > Fraction(49,6)*(2*5+3)
    paired = read('pair_signed_seed_results.json')
    assert paired['status'] == 'exact universal polynomial identities passed'
    assert len(paired['symbolic_checks']) == 5
    switch = read('pair_switch_audit_results.json')
    assert len(switch['symbolic_checks']) == 10
    assert switch['common_packet_closure'] == switch['full_tree_Local_TP2'] == 'OPEN'
    sr = switch['root']
    assert sr['e'] == [1]
    for n in range(len(sr['T'])):
        ca = sr['cA'][n] if n < len(sr['cA']) else 0
        assert sr['T'][n]-ca == sr['Te_minus_cA'][n] >= 0
        assert sr['T'][n]+ca == sr['cB'][n]

    trace = read('network_trace_audit_results.json')
    assert len(trace['checks']) == 9 and all(trace['checks'].values())
    ex = trace['abstract_exception']
    assert defects(ex['trace_minus2_halfrow']) == ex['trace_minus2_defects']
    assert ex['trace_minus2_defects'][0] == -19
    gate = read('gate_t_obstruction_results.json')
    assert gate['source_sha256'] == sha256((HERE/'gate_t_obstruction.py').read_bytes()).hexdigest()
    assert defects(gate['H_t']) == gate['delta_t'] == [334,-110,114,-18,9]
    assert defects(gate['H_X']) == gate['delta_X'] == [-6,8,-3,1]
    assert Fraction(gate['Fricke_residual'][0]) == Fraction(-7,4)
    for state in [gate['parent'], *gate['children'].values()]:
        assert all(Fraction(v) >= 0 for v in state['bounds'].values())
        assert all(Fraction(v) >= 0 for values in state['tests'].values() for v in values)
        assert all(Fraction(v) > 0 for v in state['tests']['proxy'])
        rows = {k:[Fraction(v) for v in values] for k,values in state['rows'].items()}
        assert defects(rows['G']) == [Fraction(v) for v in state['tests']['G_fold']]
        assert defects(rows['M']) == [Fraction(v) for v in state['tests']['M_fold']]
        assert minors(rows['Q'],rows['Pi']) == [Fraction(v) for v in state['tests']['proxy']]

    relative = read('falsification_relative_results.json')
    assert relative['minors'] == 3109051
    assert len(relative['records']) == 88 and not relative['failures']
    actual = read('falsification_results.json')
    assert actual['canonical_crosschecks'] == 127
    abstract = read('falsification_abstract_results.json')
    assert (abstract['tested'],abstract['accepted']) == (4185,1049)
    assert abstract['first_closure_obstruction'] is None
    assert (abstract['rational_scope']['tested'],abstract['rational_scope']['accepted']) == (1944,64)
    assert abstract['rational_scope']['first_closure_obstruction'] is None
    quantitative = read('quantitative_bandwidth_results.json')
    assert quantitative['source_sha256'] == sha256((HERE/'quantitative_bandwidth.py').read_bytes()).hexdigest()

    checked = 0
    if (HERE/'MANIFEST.json').exists():
        manifest = read('MANIFEST.json')
        assert manifest['full_tree_Local_TP2'] == 'OPEN'
        assert manifest['complete_common_predicate_closure'] == 'OPEN'
        for item in manifest['files']:
            data = (HERE/item['path']).read_bytes()
            assert len(data) == item['bytes'], item['path']
            assert sha256(data).hexdigest() == item['sha256'], item['path']
            checked += 1
    return {
        'status':'PASS',
        'scope':'Saved exact evidence, explicit seed recomputation and integrity only; not a complete replay or a formal mathematical proof.',
        'root_and_first_children_rechecked':3,
        'falsification_frozen_hashes_checked':len(frozen['files']),
        'manifest_hashes_checked':checked,
        'bounded_direct_relative_comparisons':relative['minors'],
        'actual_negative_exterior_contribution':-72,
        'naive_root_packet_defect':-388,
        'independent_trace_formal_checks':len(trace['checks']),
        'independent_paired_switch_formal_checks':len(switch['symbolic_checks']),
        'off_Fricke_auxiliary_state':'Rechecked with exact rational arithmetic; not canonical and not a P_Q closure counterexample.',
        'full_tree_Local_TP2':'OPEN',
        'complete_common_predicate_closure':'OPEN',
    }


if __name__ == '__main__':
    print(json.dumps(check(),indent=2))
