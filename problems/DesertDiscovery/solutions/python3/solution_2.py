numSpecies = int(input())

codex = dict()
for i in range(numSpecies):
    name = input()
    attrCount = int(input())
    attrs = set()
    for j in range(attrCount):
        attrs.add(input())
    codex[name] = attrs

numFossils = int(input())

for i in range(numFossils):
    attrCount = int(input())
    attrs = []
    for j in range(attrCount):
        attrs.append(input())
    
    likelihood = 50
    likelyDino = "Possible New Discovery"
    for dino in codex:
        testAttrs = codex[dino]
        M = 0
        N = 0
        for el in attrs:
            if el in testAttrs:
                M = M + 1
            else:
                N = N + 1
        prob = 100 * ((M - N)/ len(testAttrs))
        if prob >= likelihood:
            likelihood = prob
            likelyDino = dino
    print(likelyDino)
