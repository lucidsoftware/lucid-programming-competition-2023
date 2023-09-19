numLine = list(map(lambda num: int(num), input().split(' ')))
n = numLine[0]
q = numLine[1]

grid = []
for i in range(n):
    gridLine = list(map(lambda num: int(num), input().split(' ')))
    grid.append(gridLine)

sumArr = [[-1 for i in range(n)] for j in range(n)]

sumArr[0][0] = grid[0][0]
for i in range(1, n):
    sumArr[0][i] = grid[0][i] + sumArr[0][i-1]

for j in range(1, n):
    sumArr[j][0] = grid[j][0] + sumArr[j-1][0]

for i in range(1, n):
    for j in range(1, n):
        sumArr[i][j] = sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1] + grid[i][j]

for k in range(q):
    queryLine = list(map(lambda num: int(num), input().split(' ')))
    y1 = queryLine[0] - 1
    x1 = queryLine[1] - 1
    y2 = queryLine[2] - 1
    x2 = queryLine[3] - 1

    if x1 == 0 and y1 == 0:
        print(sumArr[y2][x2])
    elif x1 == 0:
        print(sumArr[y2][x2] - sumArr[y1-1][x2])
    elif y1 == 0:
        print(sumArr[y2][x2] - sumArr[y2][x1-1])
    else:
        print(sumArr[y2][x2] - sumArr[y1-1][x2] - sumArr[y2][x1-1] + sumArr[y1-1][x1-1])