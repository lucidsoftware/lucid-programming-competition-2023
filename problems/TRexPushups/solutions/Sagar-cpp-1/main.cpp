#include <iostream>
using namespace std;
int main() {
    int num_holes; cin >> num_holes;
    int places = 0, prev_hole = -1;
    for (auto i = 0; i < num_holes; i++) {
        int hole; cin >> hole;
        if (prev_hole - hole >= 4) {
            places++;
        }
        prev_hole = hole;
    }
    cout << places;
    return 0;
}
