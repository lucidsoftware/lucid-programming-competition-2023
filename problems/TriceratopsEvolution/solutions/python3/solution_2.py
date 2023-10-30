items = input().split(' ')
n = int(items[0])
g1 = float(items[1])
p0 = float(items[2])
p1 = float(items[3])
p2 = float(items[4])

g = g1
for i in range(0, n):
    none = (1 - g) * (1 - g) * p0
    one = g * (1 - g) * p1 * 2
    two = g * g * p2
    g = none + one + two

print("%.4f" % round(g, 4))