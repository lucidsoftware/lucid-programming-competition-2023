# Dino chess

# brute-force
def brute(m, n):
	seen = set()
	for i in range(n):
		for j in range(n):
			if all((i + a*m, j + b*m) not in seen for a, b in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
				seen.add((i, j))
	return len(seen)

print(brute(*map(int, input().split())))


