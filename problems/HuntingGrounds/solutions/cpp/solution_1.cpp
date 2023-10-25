#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;
int main() {
    int n, q; cin >> n >> q;
    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> grid[i][j];
        }
    }
    vector<vector<int>> grid_sum(n, vector<int>(n));
    int row_sum = 0;
    for (int i = 0; i < n; i++) {
        row_sum += grid[0][i];
        grid_sum[0][i] = row_sum;
    }
    int col_sum = 0;
    for (int i = 0; i < n; i++) {
        col_sum += grid[i][0];
        grid_sum[i][0] = col_sum;
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            grid_sum[i][j] = grid_sum[i - 1][j] + (grid_sum[i][j - 1] - grid_sum[i - 1][j -1]) + grid[i][j];
        }
    }
    for (int i = 0; i < q; i++) {
        int y1, x1, y2, x2; cin >> y1 >> x1 >> y2 >> x2; y1--; x1--; y2--; x2--;
        y1--; x1--;
        int sum = grid_sum[y2][x2];
        if (y1 >= 0) {
            sum -= grid_sum[y1][x2];
            if (x1 >= 0) {
                sum += grid_sum[y1][x1];
            }
        }
        if (x1 >= 0) {
            sum -= grid_sum[y2][x1];
        }
        cout << sum << '\n';
    }
    return 0;
}
