#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
using namespace std;
int main() {
    long long m, n; cin >> m >> n;
    long long m2 = m * 2;
    long long n2m = n / m2;
    long long mn = min(n % m2, m);
    long long a = n2m * n2m * m * m;
    long long b = mn * mn;
    long long c = n2m * 2 * mn * m;
    long long ans = a + b + c;
    cout << ans << '\n';
    return 0;
}
