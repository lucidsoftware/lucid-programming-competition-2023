# This generates a random test case for the problem
from random import randint

n = 1_000
q = 100_000
print(n, q)
for _ in range(n):
    print(*(randint(0, 1_000) for _ in range(n)))

for _ in range(q):
    y1, x1 = randint(1, n), randint(1, n)
    y2, x2 = randint(y1, n), randint(x1, n)
    print(y1, x1, y2, x2)
