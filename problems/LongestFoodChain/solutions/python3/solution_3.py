# Read in data
N = int(input())

predatorToPrey = {}

for n in range(N):
    line = input().split('<-')
    pred = line[0].strip()
    prey = [x.strip() for x in line[1].split(',')]
    predatorToPrey[pred] = prey
    for p in prey:
        predatorToPrey[p] = []

# DFS for longest chain
memo = {}
def dfs(pred):
    if pred not in memo:
        if len(predatorToPrey[pred]) == 0:
            memo[pred] = 1
        else:
            memo[pred] = 1 + max([dfs(x) for x in predatorToPrey[pred]])
    return memo[pred]


print(max([dfs(x) for x in predatorToPrey.keys()]))
