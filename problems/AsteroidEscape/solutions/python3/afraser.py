import math

sizeLine = list(map(lambda num : int(num), input().split(" ")))
n = sizeLine[0]
m = sizeLine[1]
f = sizeLine[2]

food = list(map(lambda num : int(num), input().split(" ")))
graph = [[] for el in range(n)]

for i in range(m):
    edge = list(map(lambda num : int(num), input().split(" ")))
    graph[edge[0] - 1].append(edge[1] - 1)

dp = [[-math.inf for j in range(n)] for i in range(n)]

for j in range(n):
    dp[n-1][j] = food[n-1]

for i in range(n-2, -1, -1):
    for j in range(1, n):
        for adj in graph[i]:
            dp[i][j] = max(dp[i][j], dp[adj][j-1] + food[i])

solnFound = False
for j in range(n):
    if dp[0][j] >= f:
        solnFound = True
        print(j)
        break

if not solnFound:
    print(-1)