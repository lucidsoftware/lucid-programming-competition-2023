#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
using namespace std;
int main() {
    int num_species; cin >> num_species; cin.ignore();
    unordered_map<string, unordered_set<string> > species_attributes;
    for (auto i = 0; i < num_species; i++) {
        string species; getline(cin, species);
        int num_attributes; cin >> num_attributes; cin.ignore();
        for (auto i = 0; i < num_attributes; i++) {
            string attribute; getline(cin, attribute);
            species_attributes[species].insert(attribute);
        }
    }
    int num_fossils; cin >> num_fossils; cin.ignore();
    for (auto i = 0; i < num_fossils; i++) {
        int max_likelihood_score = INT_MIN;
        string max_likelihood_score_species;
        int num_attributes; cin >> num_attributes; cin.ignore();
        vector<string> fossil_attributes; fossil_attributes.reserve(num_attributes);
        for (auto i = 0; i < num_attributes; i++) {
            string attribute; getline(cin, attribute);
            fossil_attributes.push_back(attribute);
        }
        for (auto& [species, species_attributes] : species_attributes) {
            int num_matched = 0;
            for (auto& fossil_attribute: fossil_attributes) {
                if (species_attributes.count(fossil_attribute)) {
                    num_matched++;
                }
            }
            int num_unmatched = num_attributes - num_matched;
            double likelihood_score = (100.0 * (num_matched - num_unmatched)) / species_attributes.size();
            if (likelihood_score > max_likelihood_score) {
                max_likelihood_score = likelihood_score;
                max_likelihood_score_species = species;
            }
        }
        if (max_likelihood_score >= 50.0) {
            cout << max_likelihood_score_species << '\n';
        } else {
            cout << "Possible New Discovery\n";
        }
    }
    return 0;
}
