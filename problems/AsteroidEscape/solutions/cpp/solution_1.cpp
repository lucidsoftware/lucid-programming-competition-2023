#include <bits/stdc++.h>
using namespace std;

#define umap unordered_map
#define rep(i, a, b) for(int i = a; i < (b); i++)
typedef vector<int> vi;
typedef vector<vi> vvi;

int n, m, f;
vi F;
vvi g;
umap<int, map<int, int>> ch;
void fun(int u) {
    if(ch.count(u))return;
    for(int v:g[u]){
        fun(v);
        for(auto [d,c]:ch[v])ch[u][d+1]=max(ch[u][d+1], c+F[u]);
    }
}

int main() {
    cin>>n>>m>>f;
    F.resize(n);
    g.resize(n);
    rep(i, 0, n) cin>>F[i];
    while(m--){
        int u, v;cin>>u>>v;u--,v--;
        g[u].push_back(v);
    }
    ch[n-1][0]=F[n-1];
    fun(0);
    for(auto [d, c]:ch[0])if(c>=f){
        cout<<d<<endl;
        break;
    }
}
