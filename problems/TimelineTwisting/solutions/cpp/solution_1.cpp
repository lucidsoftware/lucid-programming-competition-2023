#include <bits/stdc++.h>
using namespace std;

#define umap unordered_map
#define rep(i, a, b) for(int i = a; i < (b); i++)
typedef vector<int> vi;
typedef vector<vi> vvi;

int n, m;
vi F;
vvi g;
umap<int, int> ch;
int f(int u) {
    if(ch.count(u))return ch[u];
    int b = 0;
    for(int v:g[u]){
        b = max(b, f(v));
    }
    return ch[u] = b+F[u];
}

int main() {
    cin>>n>>m;
    F.resize(n);
    g.resize(n);
    rep(i, 0, n) cin>>F[i];
    while(m--){
        int u, v, x;cin>>u>>v>>x;
        if(x==2)swap(u, v);
        g[u].push_back(v);
    }
    
    int b = 0;
    rep(i, 0, n) b = max(b, f(i));
    cout << b << endl;
}
