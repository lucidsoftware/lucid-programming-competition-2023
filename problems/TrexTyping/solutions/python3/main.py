from collections import Counter

# Count how many times each character appears
s = input()
freq = Counter(s.lower()) # treat lowercase and uppercase versions of a letter as the same for now
freq["SHIFT"] = sum([c.isupper() for c in s]) # count how many times we have to press shift

def dist(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

home = [(0, 0), (1, 0), (4, 0), (5, 0)]
rings = 3 # how many rectangles around home row are allowed
# this is probably excessive, but just in case

# Get the distance from every key to the closest home row key
key_dists = []
for i in range(-rings, rings+1):
    for j in range(-rings, rings+6):
        key_dists.append(min([dist(j, i, *k) for k in home]))
key_dists.sort()

# Put the most common characters on the closest keys
total = 0
for (i, (_, f)) in enumerate(freq.most_common()):
    total += key_dists[i] * f
print(round(total * 2, 3)) # Be sure to double the distance (there and back)
