#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
struct Node {
    Node *parent = NULL;
    string name;
    Node(string name_) {
        name = name_;
    }
};
vector<string> get_path(Node *node) {
    vector<string> path;
    while (node) {
        path.push_back(node->name);
        node = node->parent;
    }
    reverse(path.begin(), path.end());
    return path;
}
string lca(const vector<string>& left_path, const vector<string>& right_path) {
    string common;
    int i = 0;
    while (left_path[i] == right_path[i]) {
        common = left_path[i];
        i++;
    }
    return common;
}
int main() {
    int num_relationships; cin >> num_relationships; cin.ignore();
    const string delimiter = " -- ";
    unordered_map<string, Node*> nodes;
    for (auto i = 0; i < num_relationships; i++) {
        string line; getline(cin, line);
        auto position = line.find(delimiter);
        string ancestor = line.substr(0, position);
        string descendent = line.substr(position + delimiter.size());
        if (!nodes.count(ancestor)) {
            nodes[ancestor] = new Node(ancestor);
        }
        if (!nodes.count(descendent)) {
            nodes[descendent] = new Node(descendent);
        }
        (nodes[descendent])->parent = nodes[ancestor];
    }
    string left; getline(cin, left);
    string right; getline(cin, right);
    auto left_path = get_path(nodes[left]);
    auto right_path = get_path(nodes[right]);
    cout << lca(left_path, right_path);
    return 0;
}
