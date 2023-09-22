bx, by = map(int, input().split())
n = int(input())
dinos = [(map(int, input().split())) for _ in range(n)]
offset = [(x - bx, y - by) for x, y in dinos]

quad = lambda x, y : (x > 0) << 1 + (y > 0)
div = lambda x, y : float("inf") if y == 0 else x / y

print(len(set((quad(x, y), div(x, y)) for x, y in offset)))
