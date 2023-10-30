#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
using namespace std;
int main() {
    int num_responses; cin >> num_responses; cin.ignore();
    int beloved_dinosaur_votes = 0;
    string beloved_dinosaur_name;
    unordered_map<string,int> dinosaur_votes;
    for (auto i = 0; i < num_responses; i++) {
        string response, dinosaur;
        getline(cin, response);
        istringstream ss(response);
        while (getline(ss, dinosaur, ',')) {
            dinosaur_votes[dinosaur]++;
            if (dinosaur_votes[dinosaur] > beloved_dinosaur_votes) {
                beloved_dinosaur_votes = dinosaur_votes[dinosaur];
                beloved_dinosaur_name = dinosaur;
            }
        }
    }
    cout << beloved_dinosaur_name << '\n';
    cout << beloved_dinosaur_votes << '\n';
    return 0;
}
