#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); i++)
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

int h, w, n;
vvi vs;

struct State {
    vi dims;
    vvi g, placements;
    int areaLeft;
    State(int h, int w): g(h, vi(w)) {dims={h,w}; areaLeft = h*w;}

    pii score(){return {placements.size(), -areaLeft};}

    void assertDims(vi &loc, vi &sz) {
        rep(i, 0, 2) assert(0<=loc[i]&&loc[i]+sz[i]<=dims[i]);
    }
    void put(vi &loc, vi &sz) {
        assertDims(loc, sz);
        rep(i, 0, sz[0])rep(j, 0, sz[1])assert(++g[loc[0]+i][loc[1]+j]==1);
        placements.push_back({loc[0], loc[1], sz[0], sz[1]});
        areaLeft -= sz[0]*sz[1];
    }
    void unput(vi &loc, vi &sz) {
        assertDims(loc, sz);
        rep(i, 0, sz[0])rep(j, 0, sz[1])assert(--g[loc[0]+i][loc[1]+j]==0);
        placements.pop_back();
        areaLeft += sz[0]*sz[1];
    }

    bool isempty(int si, int sj, vi &sz){
        rep(i, 0, sz[0])rep(j, 0, sz[1])if(g[si+i][sj+j]) return false;
        return true;
    }
    vvi posslocs(vi&sz){
        vvi res;
        rep(i, 0, dims[0]-sz[0]+1)rep(j, 0, dims[1]-sz[1]+1)if(isempty(i, j, sz))res.push_back({i,j});
        return res;
    }
};

State beststate(0,0);

void nfits(int vsi, State &state) {
    if(vsi == n){
        if(state.score() > beststate.score())beststate=state;
        return;
    }

    nfits(vsi+1, state);

    vvi locs = state.posslocs(vs[vsi]);
    for(vi&loc:locs){
        state.put(loc, vs[vsi]);
        nfits(vsi+1, state);
        state.unput(loc, vs[vsi]);
    }
}

int main() {
    cin>>h>>w>>n;
    vs.assign(n, vi(2));
    rep(i, 0, n)rep(j, 0, 2)cin>>vs[i][j];
    State state(h, w);
    nfits(0, state);
    cout << beststate.score().first << ' ' << -beststate.score().second << endl;
    // cout<<"SPOTS:\n";
    // for(vi&pl:beststate.placements){
    //     for(int v:pl)cout<<v<<' ';
    //     cout<<endl;
    // }
}
