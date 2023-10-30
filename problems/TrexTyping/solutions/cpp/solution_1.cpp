#include <bits/stdc++.h>
using namespace std;

#define umap unordered_map
#define rep(i, a, b) for(int i = a; i < (b); i++)
#define all(x) begin(x), end(x)

double d(double x1, double y1, double x2, double y2){
    return sqrt(pow(x1-x2, 2)+pow(y1-y2, 2));
}
double d(double x, double y){
    double r = 1e6;
    r = min(r, d(x, y, 0, 0));
    r = min(r, d(x, y, 1, 0));
    r = min(r, d(x, y, 4, 0));
    r = min(r, d(x, y, 5, 0));
    return r;
}

char const SHIFT = '\0';
int main() {
    string w;
    umap<char, int> freq;
    getline(cin, w);
    for(char c:w){
        if(isupper(c))freq[SHIFT]++, c=tolower(c);
        freq[c]++;
    }

    vector<double> fs, ds;
    // 26*2+10+10 < 100
    rep(x, -100, 100)rep(y, -100, 100)ds.push_back(d(x, y));
    sort(all(ds));
    for(auto [c, f]:freq){
        fs.push_back(f);
    }
    sort(all(fs));
    reverse(all(fs));
    auto it=ds.begin();
    double r = 0;
    for(double f:fs)r+=f**it++;
    r*=2;

    // this method actually matches the current expected output
    r=round(r*1000)/1000;
    stringstream ss;
    ss<<fixed<<r;
    string s=ss.str();
    while(s.back()=='0')s.pop_back();
    if(s.back()=='.')s.push_back('0');
    cout<<s<<endl;

    // // this didn't work, but if we change the python solution to the code below, it will match
    // cout<<fixed<<setprecision(3)<<r<<endl;
    // // python equivalent (replace the current print line with this):
    // // print(f'{total*2:.3f}') # Be sure to double the distance (there and back)
}
