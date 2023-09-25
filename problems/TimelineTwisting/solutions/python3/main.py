from typing import List

# Read input, construct graph
n, c = map(int, input().split())
d = list(map(int, input().split()))
g = [{} for _ in range(n)]
for _ in range(c):
    x, y, z = map(int, input().split())
    if z == 1:
        g[x][y] = d[x]
    elif z == 2:
        g[y][x] = d[y]


visited = [False] * n
order = []
def dfs(node: int):
    visited[node] = True
    for neighbor in g[node]:
        if not visited[neighbor]:
            dfs(neighbor)
    order.append(node)


def get_max_path(order: List[int]) -> int:
    dist = [0] * n
    for node in order:
        dist[node] += d[node]
        for neighbor in g[node]:
            dist[neighbor] = max(dist[neighbor], dist[node])

    return max(dist)


for src in range(n):
    dfs(src)
order = order[::-1]

# The answer is the longest path length
print(get_max_path(order))
