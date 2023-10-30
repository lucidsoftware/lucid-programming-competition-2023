#include <bits/stdc++.h>
using namespace std;

#define umap unordered_map
#define rep(i, a, b) for(int i = a; i < (b); i++)
typedef vector<int> vi;
typedef pair<int, int> pii;

int H, W, n;
vector<pair<int, int>> dims;
vi ms;

vector<umap<int, pii>> ch;
vector<umap<int, pair<int, int>>> pl;
vector<umap<int, int>> plm;
pii f(int msi, int a){
    if(msi==n)return {0, 0};
    if(ch[msi].count(a))return ch[msi][a];

    pii r = f(msi+1, a);
    int m = ms[msi];
    pl[msi][a]={-1,-1};
    plm[msi][a]=0;

    rep(i, 0, H-dims[msi].first+1)rep(j, 0, W-dims[msi].second+1){
        int sm = m<<(i*W+j);
        if (!(a&sm)){
            pii h = f(msi+1, a|sm);
            h.first++;
            h.second+=dims[msi].first*dims[msi].second;
            if(h>r){
                pl[msi][a]={i,j};
                plm[msi][a]=sm;
                r=h;
            }
        }
    }

    return ch[msi][a] = r;
}

int main() {
    cin>>H>>W>>n;
    ch.resize(n);
    pl.resize(n);
    plm.resize(n);
    rep(i, 0, n) {
        int h, w;cin>>h>>w;
        int m=0, one = (1<<w)-1;
        rep(k, 0, h)m|=one<<(W*k);
        ms.push_back(m);
        dims.emplace_back(h, w);
    }

    auto [k, u] = f(0,0);
    cout<<k<<' '<<H*W-u<<endl;

    // cout<<"SPOTS:\n";
    // int a = 0;
    // rep(i, 0, n){
    //     if(plm[i][a]){
    //         cout<<pl[i][a].first<<' '<<pl[i][a].second<<' '<<dims[i].first<<' '<<dims[i].second<<endl;
    //     }
    //     a|=plm[i][a];
    // }
    return 0;
}
