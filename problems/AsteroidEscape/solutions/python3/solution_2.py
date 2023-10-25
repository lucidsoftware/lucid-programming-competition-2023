from collections import deque

n, m, f = [int(x) for x in input().split()]
adjacency_list = [[] for _ in range(n)]
foods = [int(x) for x in input().split()]
for _ in range(m):
    source, dest = [int(x) for x in input().split()]
    source -= 1
    dest -= 1
    adjacency_list[source].append(dest)


def bfs():
    visited = {0: foods[0]}
    queue = deque([(0, 0, foods[0])])
    while queue:
        current, current_distance, current_food = queue.popleft()
        for next in adjacency_list[current]:
            next_distance = current_distance + 1
            next_food = current_food + foods[next]

            if next == n-1:
                if next_food >= f:
                    return next_distance

            if next not in visited or visited[next] < next_food:
                visited[next] = next_food
                queue.append((next, next_distance, next_food))
    return -1


print(bfs())
