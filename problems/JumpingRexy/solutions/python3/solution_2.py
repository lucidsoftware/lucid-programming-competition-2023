from collections import deque

max_jumps = 5
directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

m, n = [int(x) for x in input().split()]
grid = [input().split() for _ in range(m)]

def find_start(m, n, grid):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'D':
                return i, j

def bfs(m, n, grid):
    start_i, start_j = find_start(m, n, grid)
    visited = {(start_i, start_j): max_jumps}
    queue = deque([(start_i, start_j, 0, max_jumps)])
    while queue:
        current_i, current_j, distance, current_jumps_left = queue.popleft()
        for (d_i, d_j) in directions:
            next_i, next_j = current_i + d_i, current_j + d_j
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n or grid[next_i][next_j] == 'B' or grid[next_i][next_j] == 'D':
                continue
            next_jumps_left = current_jumps_left
            if grid[next_i][next_j] == 'P':
                if next_i == 0 or next_j == 0 or next_i == m - 1 or next_j == n - 1:
                    return distance + 1
            elif grid[next_i][next_j] == 'C':
                next_jumps_left -= 1
            if next_jumps_left < 0:
                continue
            if (next_i, next_j) not in visited or visited[(next_i, next_j)] < next_jumps_left:
                visited[(next_i, next_j)] = next_jumps_left
                queue.append((next_i, next_j, distance + 1, next_jumps_left))
    return -1

print(bfs(m, n, grid))
