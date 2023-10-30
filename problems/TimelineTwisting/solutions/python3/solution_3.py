from collections import deque

n, c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
incoming_nodes = [[] for _ in range(n)]
distance = [-1 for _ in range(n)]

for _ in range(c):
    x, y, z = [int(a) for a in input().split()]
    if z == 2:
        y, x = x, y
    incoming_nodes[y].append(x)


def dfs(node):
    if distance[node] != -1:
        return distance[node]
    incoming_max = 0
    for incoming_node in incoming_nodes[node]:
        incoming_max = max(incoming_max, dfs(incoming_node))
    distance[node] = incoming_max + d[node]
    return distance[node]


max_time = 0
for node in range(n):
    max_time = max(max_time, dfs(node))

print(max_time)
