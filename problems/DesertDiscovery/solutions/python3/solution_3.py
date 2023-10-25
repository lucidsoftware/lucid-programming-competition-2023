S = int(input())
species = []
for s in range(S):
    name = input()
    attributes = set()
    for a in range(int(input())):
        attributes.add(input().strip())
    species.append((name, attributes))

F = int(input())
for f in range(F):
    attributes = set()
    for a in range(int(input())):
        attributes.add(input().strip())
    bssf = ('asdf', 0.0)
    for name, speciesAttributes in species:
        M, N = 0, 0
        for attr in attributes:
            if attr in speciesAttributes:
                M += 1
            else:
                N += 1
        score = 100 * (M - N) / len(speciesAttributes)
        if score > bssf[1]:
            bssf = (name, score)
    if bssf[1] < 50:
        print("Possible New Discovery")
    else:
        print(bssf[0])
