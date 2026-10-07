// Exact tensor-Bernstein certificate for eight independent quadratic factors.
// Uses S_8 symmetry: a Bernstein index is an unordered multiset of eight
// pairs (a,b) in {0,1,2}^2. There are C(16,8)=12870 such indices.
// Each local tensor is scaled by 64. All intermediate coefficients are
// nonnegative and their sum is at most 17956^8. Therefore every signed
// margin below has absolute value <=513*17956^8 < 2^127-1.
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using I=__int128_t;
struct Term {int i,j; I c;};
struct Grid {int d; std::vector<I> a;};
std::array<std::vector<Term>,9> local;
std::array<int,9> count{};
std::array<I,17> minima;
std::array<std::array<int,9>,17> witnesses{};
long long cases=0, negative=0, zero=0;

std::string decimal(I x) {
    if(x==0) return "0";
    bool neg=x<0; if(neg)x=-x;
    std::string s; while(x){s.push_back(char('0'+x%10));x/=10;}
    if(neg)s.push_back('-');std::reverse(s.begin(),s.end());return s;
}
I get(const Grid& g,int i,int j) {
    if(i < -g.d || i > g.d || j < -g.d || j > g.d) return 0;
    return g.a[(i+g.d)*(2*g.d+1)+j+g.d];
}
Grid times(const Grid& p, int type) {
    Grid out{p.d+2,std::vector<I>((2*p.d+5)*(2*p.d+5),0)};
    int oldw=2*p.d+1,neww=2*out.d+1;
    for(int i=-p.d;i<=p.d;++i)for(int j=-p.d;j<=p.d;++j){
        I v=p.a[(i+p.d)*oldw+j+p.d];
        if(v==0)continue;
        for(auto t:local[type])out.a[(i+t.i+out.d)*neww+j+t.j+out.d]+=v*t.c;
    }
    return out;
}
void visit(int depth,int first,const Grid& p) {
    if(depth==8){
        ++cases;
        for(int n=0;n<=16;++n){
            I diag=get(p,n,n);
            I delta=diag-get(p,n-1,n+1)-get(p,n+1,n+1)+get(p,n,n+2);
            I margin=128*delta-diag;
            if(margin<0)++negative;
            if(margin==0)++zero;
            if(margin<minima[n]){minima[n]=margin;witnesses[n]=count;}
        }
        return;
    }
    for(int t=first;t<9;++t){++count[t];auto q=times(p,t);visit(depth+1,t,q);--count[t];}
}
int main(){
    // f0=4x^2+12x+5, fu=4x+10, fv=4 in Laurent half-rows.
    const std::array<int,5> f0{4,12,13,12,4};
    const std::array<int,5> fu{0,4,10,4,0};
    const std::array<int,5> fv{0,0,4,0,0};
    for(int a=0;a<=2;++a)for(int b=0;b<=2;++b){
        int type=3*a+b;
        for(int i=0;i<5;++i)for(int j=0;j<5;++j){
            I c=4*f0[i]*f0[j]
                +2*a*(fu[i]*f0[j]+f0[i]*fu[j])
                +2*b*(fv[i]*f0[j]+f0[i]*fv[j])
                +2*a*(a-1)*fu[i]*fu[j]
                +a*b*(fu[i]*fv[j]+fv[i]*fu[j])
                +2*b*(b-1)*fv[i]*fv[j];
            if(c)local[type].push_back({i-2,j-2,c});
        }
    }
    I infinity=(I(1)<<126);
    for(auto &v:minima)v=infinity;
    visit(0,0,Grid{0,{1}});
    std::cout<<"{\n  \"status\":\""<<(negative==0 && zero==0?"PASS":"FAIL")<<"\",\n";
    std::cout<<"  \"patterns\":"<<cases<<",\n  \"distinct_Bernstein_margins\":"<<17*cases<<",\n";
    std::cout<<"  \"negative_coefficients\":"<<negative<<",\n  \"zero_coefficients\":"<<zero<<",\n";
    std::cout<<"  \"scaling\":\"64^8 times the Bernstein coefficient of 128 delta_n(P)-H(P)_n^2\",\n";
    std::cout<<"  \"minimum_by_index\":[\n";
    for(int n=0;n<=16;++n){
        std::cout<<"    {\"n\":"<<n<<",\"minimum\":\""<<decimal(minima[n])<<"\",\"histogram\":[";
        for(int t=0;t<9;++t){if(t)std::cout<<",";std::cout<<witnesses[n][t];}
        std::cout<<"]}"<<(n<16?",":"")<<"\n";
    }
    std::cout<<"  ]\n}\n";
    return negative==0 && zero==0 && cases==12870?0:1;
}
