# This is uses to analyze the size of randomly generated tests
# Specifically how many units the queries cover
# This is how many additions a brute force c++ solution would have to perform

n, q = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

total = 0
for y1, x1, y2, x2 in queries:
    total += (y2+1-y1) * (x2+1-x1)

print(f'{total:,}')