N = int(input())
graph = dict()
sources = set()

for i in range(N):
    (dest, srcs) = input().split("<-")
    dest = dest.strip()
    srcs = map(lambda x: x.strip(), srcs.split(','))
    if dest not in graph:
        graph[dest] = []
    if dest in sources:
        sources.remove(dest)
    for el in srcs:
        if el not in graph:
            graph[el] = []
            sources.add(el)
        
        graph[el].append(dest)

def dfs(currNode, dist):
    maxDist = dist
    for adj in graph[currNode]:
        maxDist = max(dfs(adj, dist + 1), maxDist)
    return maxDist

maxDist = -1
for el in sources:
    maxDist = max(dfs(el, 0), maxDist)

print(maxDist + 1)