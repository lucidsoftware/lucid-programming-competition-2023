# Dino chess

# How many dinos can fit on an N x N board?
def dinoCount(m, n):
	out = 0
	for i in range(m):
		for j in range(m):
			out += kingCount(-((n - i) // -m), -((n - j) // -m))
	return out

# How many kings can fit on an L x K board?
def kingCount(l, k):
	return ((l+1) // 2) * ((k+1) // 2)

print(dinoCount(*map(int, input().split())))
