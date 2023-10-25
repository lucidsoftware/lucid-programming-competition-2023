#include <bits/stdc++.h>
using namespace std;

#define umap unordered_map
#define rep(i, a, b) for(int i = a; i < (b); i++)
typedef vector<int> vi;
typedef vector<vi> vvi;

int n, m, f;
vi F;
vvi g;
vector<umap<int, int>> ch;
int fun(int u, int fr){
    fr=max(0, fr-F[u]);
    if(ch[u].count(fr))return ch[u][fr];
    if(u==n-1)return fr==0?0:INT_MAX/2;
    int b = INT_MAX/2;
    for(int v:g[u])b=min(b, 1+fun(v, fr));
    return ch[u][fr]=b;
}

int main() {
    cin>>n>>m>>f;
    F.resize(n);
    g.resize(n);
    ch.resize(n);
    rep(i, 0, n) cin>>F[i];
    while(m--){
        int u, v;cin>>u>>v;u--,v--;
        g[u].push_back(v);
    }
    cout << fun(0, f) << endl;
}
