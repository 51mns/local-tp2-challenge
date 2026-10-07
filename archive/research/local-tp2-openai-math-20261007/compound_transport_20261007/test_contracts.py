"""Finite regression tests and negative controls; not the infinite proof."""
import unittest
from fractions import Fraction as F
import author as a


def det(m):return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def madd(m,n):return [[m[i][j]+n[i][j] for j in range(2)] for i in range(2)]


class Contracts(unittest.TestCase):
    def test_scalar_failure_and_full_interval_channel_certificate(self):
        r=a.ray('', 'R');h=a.H(a.sub(r['t'],(2,)))
        self.assertEqual(F(a.delta(h)[0],a.mass(a.sub(r['t'],(2,)))),F(1,16))
        result=a.build('', 'R')
        self.assertEqual(result['summary']['tail_starts'],2)
        self.assertEqual(result['arrays']['channel_0'],['82','36','6'])
        self.assertEqual(result['arrays']['final_proxy_budget'],['6057/16'])
        self.assertEqual(result['arrays']['final_multiplier_budget'],['2457/16'])

    def test_mixed_terms_cannot_be_omitted_without_loss(self):
        # A fixed matrix split into M equal summands: diagonals alone lose 1/M.
        m=[[2,1],[1,2]]
        for count in [2,5,40]:
            lam=F(1,count)
            diagonal=count*lam*lam*det(m)
            mixed=F(count*(count-1),2)*lam*lam*(det(madd(m,m))-2*det(m))
            self.assertEqual(diagonal,F(det(m),count))
            self.assertEqual(diagonal+mixed,det(m))

    def test_positive_individual_minors_do_not_imply_positive_mixture(self):
        m=[[4,8],[1,4]];n=[[4,1],[8,4]]
        self.assertEqual((det(m),det(n),det(madd(m,n))),(8,8,-17))
        self.assertEqual(det(madd(m,n))-det(m)-det(n),-33)

    def test_channel_truncation_is_lower_bound_not_equality(self):
        t=a.ray('', 'R')['t'];f=a.sub(t,(-2,));g=a.sub(t,(2,))
        hf,hg,hfg=a.H(f),a.H(g),a.H(a.mul(f,g))
        low=[[sum(a.minor(hf,i,k)*a.minor(hg,k,j) for k in range(4)) for j in range(4)] for i in range(4)]
        gaps=[a.minor(hfg,i,j)-low[i][j] for i in range(4) for j in range(4)]
        self.assertGreaterEqual(min(gaps),0)
        self.assertGreater(max(gaps),0)

    def test_interpolation_nodes_are_not_a_positivity_proof(self):
        f=lambda u:(u-F(1,4))**2-F(1,100)
        nodes=[f(u) for u in [F(0),F(1,2),F(1)]]
        self.assertGreater(min(nodes),0)
        self.assertLess(f(F(1,4)),0)
        self.assertLess(min(a.bern({(j,):v for j,v in enumerate(nodes)},1)),0)

    def test_mixed_mass_bound_at_arbitrary_rational_weights(self):
        # Not a canonical path: checks the genuinely general mixture identity.
        for word,direction in [('', 'R'),('LRL','R')]:
            r=a.ray(word,direction);A,B,t=r['A'],r['B'],r['t']
            roots=(-2,0,2);weights=(F(1,2),F(1,3),F(1,6));Z=(0,)
            for i,root in enumerate(roots):
                z=a.add(a.mul(A,a.sub(t,(root,))),B)
                for j,rj in enumerate(roots):
                    if j!=i:z=a.mul(z,a.sub(t,(rj,)))
                Z=a.add(Z,a.scale(z,weights[i]))
            report=a.build(word,direction)['summary'];cp=F(report['c_proxy']);cm=F(report['c_multiplier'])
            for n in range(report['channels']):
                self.assertGreaterEqual(a.W(a.mul(r['J'],Z),a.mul(r['V'],Z),n),cp*4*a.mass(Z))
                self.assertGreaterEqual(a.delta(a.H(a.mul(a.mul(a.y,a.y),Z)))[n],cm*4*a.mass(Z))

    def test_terminal_degree_and_original_target_regression(self):
        for prefix,direction in [('', 'R'),('LRL','R')]:
            r=a.ray(prefix,direction);ad,bd=len(r['X'])-1,len(r['Y'])-1
            for N in range(1,6):
                X,C,Y=a.state(prefix+direction*N)
                U,V=sorted((a.mutate(X,C,Y),a.mutate(Y,C,X)),key=len)
                S,D=a.sub(U,C),a.sub(V,U)
                self.assertEqual(len(D)-len(S),bd+1+(N-1)*(ad+1))
                self.assertGreater(min(a.W(S,D,n) for n in range(len(S))),0)


if __name__=='__main__':unittest.main(verbosity=2)
