(m, n) = map(lambda x: int(x), input().split(','))

grid = []
for i in range(m):
    grid.append([c for c in input()])

start = (-1, -1)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if(grid[i][j].isalpha()):
            grid[i][j] = ord(grid[i][j]) - 64
        if(grid[i][j] == '@'):
            start = (i, j)
        

def adj(row, col):
    adjList = []
    if row != 0:
        adjList.append((row - 1, col))
    if row != len(grid) - 1:
        adjList.append((row + 1, col))
    if col != 0:
        adjList.append((row, col - 1))
    if col != len(grid[0]) - 1:
        adjList.append((row, col + 1))
    return adjList

def dfs(row, col, steps, energy, size, stomach):
    if steps == 11 or energy < 0:
        return size
    
    energyUse = 1
    if grid[row][col] == '~' or grid[row][col] == '"':
        energyUse = 2
    if grid[row][col] == '*':
        energyUse = 3
    
    if grid[row][col] == '#' and grid[row][col] == '^' and grid[row][col] == '&':
        return size
    
    oldValue = grid[row][col]
    if isinstance(grid[row][col], int):
        if size >= grid[row][col]:
            stomach = stomach + grid[row][col]
            energy = min(energy + grid[row][col], size)
            grid[row][col] = '.'
            if stomach >= size:
                stomach = stomach - size
                size = size + 1
                energy = size
        else:
            return size
    
    bestSize = size
    for (destRow, destCol) in adj(row, col):
        bestSize = max(bestSize, dfs(destRow, destCol, steps + 1, energy - energyUse, size, stomach))
    
    grid[row][col] = oldValue
    return bestSize

print(dfs(start[0], start[1], 0, 1, 1, 0))