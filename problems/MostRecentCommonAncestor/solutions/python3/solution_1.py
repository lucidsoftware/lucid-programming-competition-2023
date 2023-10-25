# Read in data
N = int(input())

childToParent = {}
for n in range(N):
    anc, des = [x.strip() for x in input().split('--')]
    childToParent[des] = anc
    if anc not in childToParent:
        childToParent[anc] = None

f = input()
s = input()
visited = set()
while f:
    visited.add(f)
    f = childToParent[f]

while s:
    if s in visited:
        print(s)
        break
    s = childToParent[s]
