from collections import deque
from typing import List

def shortest_distance_with_jumps(grid: List[List[str]]) -> int:
    n, m = len(grid), len(grid[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    visited = [[[-1] * 6 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'D':
                start = (i, j)
                visited[i][j][0] = 0
    
    queue = deque([(start[0], start[1], 0)])  # (x, y, jumps)
    
    while queue:
        x, y, jumps = queue.popleft()
        if (x == 0 or y == 0 or x == n - 1 or y == m - 1) and grid[x][y] == 'P':  # If at the edge
            return visited[x][y][jumps]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 'P' and visited[nx][ny][jumps] == -1:
                    visited[nx][ny][jumps] = visited[x][y][jumps] + 1
                    queue.append((nx, ny, jumps))
                elif grid[nx][ny] == 'C' and jumps < 5 and visited[nx][ny][jumps + 1] == -1:
                    visited[nx][ny][jumps + 1] = visited[x][y][jumps] + 1
                    queue.append((nx, ny, jumps + 1))

    return -1  # No path found


def read_input():
    N, M = map(int, input().strip().split())
    grid = [list(input().strip().split()) for _ in range(N)]
    return grid

grid = read_input()
print(shortest_distance_with_jumps(grid))
