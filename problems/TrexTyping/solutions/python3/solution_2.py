import math
from collections import defaultdict

keys = sorted((
    [0.0] * 4
    + [1.0] * 12
    + [2.0] * 10
    + [3.0] * 10
    + [math.sqrt(2)] * 8
    + [math.sqrt(5)] * 12
    + [math.sqrt(8)] * 4
    + [math.sqrt(10)] * 12
))

SHIFT = "SHIFT"
charFrequencies = defaultdict(int)
for char in input():
    if char.isupper():
        # press shift, press letter, press shift
        charFrequencies[SHIFT] += 1
    # press letter
    charFrequencies[char.lower()] += 1
dist = 0.0

for i, (_, count) in enumerate(sorted(charFrequencies.items(), key=lambda x: x[1], reverse=True)):
    dist += keys[i] * count * 2  # count distance to and from key

print(round(dist, 3))
