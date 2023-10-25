#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;
int n, m, max_size = 1, max_steps = 10;
const vector<pair<int, int>> directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
unordered_map<string, char> visited_energy;
struct state {
  vector<string> grid;
  char i, j, size, eaten, energy;
};
string get_hash(const state& s) {
  string hash;
  for (int i = 0; i < n; i++) {
    hash += s.grid[i];
  }
  hash += s.i; hash += s.j; hash += s.size; hash += s.eaten;
  return hash;
}
void print_hash(const string& s) {
  cout << "hash:\n";
  int s_length = s.length();
  cout << s.substr(0, s_length - 4);
  cout << ' ' << int(s[s_length - 4]) << ' ' << int(s[s_length - 3]);
  cout << ' ' << int(s[s_length - 2]) << ' ' << int(s[s_length - 1]);
  cout << '\n';
}
state read_state() {
  string line; getline(cin, line);
  auto comma = line.find(',');
  n = stoi(line.substr(0, comma));
  m = stoi(line.substr(comma + 1));
  state s; s.size = 1; s.energy = 1; s.eaten = 0;
  s.grid = vector<string>(n);
  for (int i = 0; i < n; i++) {
    getline(cin, s.grid[i]);
    for (int j = 0; j < n; j++) {
      if (s.grid[i][j] == '@') {
        s.i = i; s.j = j;
      }
    }
  }
  return s;
};
void print_state(state& s) {
  cout << "\ngrid: \n";
  for (int i = 0; i < n; i++) {
    cout << s.grid[i] << '\n';
  }
  cout << "i: " << int(s.i) << ", j: " << int(s.j) << ", size: " << int(s.size) << ", eaten: " << int(s.eaten) << ", energy: " << int(s.energy) << "\n\n";
}
void solve_bfs(state initial) {
  queue<state> q;
  q.push(initial); visited_energy[get_hash(initial)] = initial.energy;
  int level = 0;
  while (!q.empty() && (level++) < max_steps) {
    int level_size = q.size();
    for (int z = 0; z < level_size; z++) {
      state current = q.front(); q.pop();
      for (auto& [di, dj]: directions) {
        state next;
        next.i = current.i + di; next.j = current.j + dj;
        if (next.i < 0 || next.j < 0 || next.i == n || next.j == m) {
          continue;
        }
        char cell = current.grid[next.i][next.j];
        if (cell == '#' || cell == '^' || cell == '&') {
          continue;
        }
        next.size = current.size; next.energy = current.energy;
        if (cell >= 'A' && cell <= 'Z') {
          char opponent_size = cell - 'A' + 1;
          if (opponent_size > current.size) {
            continue;
          }
          next.grid = current.grid;
          next.eaten = current.eaten + opponent_size;
          if (next.eaten >= next.size) {
            next.size = min(next.size + 1, 26);
            next.eaten = 0;
          }
          next.energy = next.size;
        } else {
          next.grid = current.grid;
          next.eaten = current.eaten;
          if (cell == '*') {
            next.energy -= 3;
          } else if (cell == '~' || cell == '"') {
            next.energy -= 2;
          } else if (cell == '.') {
            next.energy -= 1;
          }
        }
        next.grid[next.i][next.j] = '@';
        next.grid[current.i][current.j] = '.';
        bool add_to_queue = false;
        if (next.energy > 0) {
          if (visited_energy.count(get_hash(next))) {
            auto previous_visit_energy = visited_energy[get_hash(next)];
            if (next.energy > previous_visit_energy) {
              add_to_queue = true;
            }
          } else {
            add_to_queue = true;
          }
          if (add_to_queue) {
            max_size = max(max_size, int(next.size));
            q.push(next); visited_energy[get_hash(next)] = next.energy;
          } else {
          }
        }
      }
    }
  }
}
int main() {
  state initial = read_state();
  solve_bfs(initial);
  cout << max_size << '\n';
  return 0;
}
