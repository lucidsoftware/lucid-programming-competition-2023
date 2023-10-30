#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;
int main() {
    int num_pieces, num_dinos, min_land;
    cin >> num_pieces >> num_dinos >> min_land;
    vector<int> pieces; pieces.reserve(num_pieces);
    for (auto i = 0; i < num_pieces; i++) {
        int piece; cin >> piece;
        pieces.push_back(piece);
    }
    sort(pieces.begin(), pieces.end());
    vector<int> pieces_sum; pieces_sum.reserve(num_pieces);
    int sum = 0;
    for (auto piece: pieces) {
        sum += piece;
        pieces_sum.push_back(sum);
    }
    int total_sum = pieces_sum[num_pieces - 1];
    int min_difference = INT_MAX;
    for (auto i = 0; i < num_pieces - num_dinos + 1; i++) {
        int j = i + num_dinos - 1;
        int subarray_sum = (i == 0) ? pieces_sum[j] : pieces_sum[j] - pieces_sum[i - 1];
        int remaining_sum = total_sum - subarray_sum;
        if (remaining_sum >= min_land) {
            int difference = pieces[j] - pieces[i];
            min_difference = min(min_difference, difference);
        }
    }
    cout << min_difference << '\n';
    return 0;
}
