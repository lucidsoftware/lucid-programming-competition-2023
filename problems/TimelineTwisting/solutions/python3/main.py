# Read input, construct graph
n, c = map(int, input().split())
d = list(map(int, input().split()))
g = [{} for _ in range(n)]
in_count = [0 for _ in range(n)]
for _ in range(c):
    x, y, z = map(int, input().split())
    if z == 1:
        g[x][y] = d[x]
        in_count[y] += 1
    elif z == 2:
        g[y][x] = d[y]
        in_count[x] += 1
    elif z == 3:
        g[x][y] = d[x]
        g[y][x] = d[y]
        # we don't increase in_count here since we can still use either as a source later



# From each "source" species, we need to find the longest path through the graph
# The answer is the max of those path lengths
