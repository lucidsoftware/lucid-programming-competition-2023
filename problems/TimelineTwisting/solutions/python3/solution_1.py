

(n, c) = map(lambda x: int(x), input().split())
durations = list(map(lambda x: int(x), input().split()))
graph = [[] for i in range(n)]

for i in range(c):
    (x, y, invert) = map(lambda x: int(x), input().split())
    if invert == 1:
        graph[x].append(y)
    else:
        graph[y].append(x)

visited = set()
postOrder = list()
def traverse(currNode):
    if currNode in visited:
        return
    
    visited.add(currNode)
    for adj in graph[currNode]:
        traverse(adj)
    postOrder.append(currNode)

for vert in range(n):
    traverse(vert)

cache = [-1 for i in range(n)]
for vert in postOrder:
    cache[vert] = durations[vert] + max([0] + [cache[adj] for adj in graph[vert]])

print(max(cache))