inputs = input().split()
n, g1, p0, p1, p2 = [float(value) for value in inputs]

for i in range(int(n)):
    none = (1 - g1)**2 * p0
    one = g1 * (1 - g1) * 2 * p1
    both = g1**2 * p2
    g1 = none + one + both

print("%.4f" % round(g1, 4))
