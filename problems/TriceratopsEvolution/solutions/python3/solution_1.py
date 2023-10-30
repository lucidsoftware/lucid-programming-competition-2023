line = input().split(' ')

N = int(line[0])
g1 = float(line[1])
p0 = float(line[2])
p1 = float(line[3])
p2 = float(line[4])

iterations = N
traitProb = g1

for i in range(iterations):
    both = traitProb**2
    one = traitProb * (1 - traitProb) * 2
    neither = (1 - traitProb)**2

    traitProb = (both * p2) + (one * p1) + (neither * p0)

print("%.4f" % round(traitProb, 4))
