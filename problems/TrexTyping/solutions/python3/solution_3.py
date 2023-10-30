import math

def incrementKey(inputMap, key):
    if key in inputMap:
        inputMap[key] = inputMap[key] + 1
    else:
        inputMap[key] = 1

# Number of keys possible at a,b dist (x/y agnostic) on an ortholinear keyboard
def numKeys(a, b):
    if a == 0 and b == 0:
        return 4
    if a + b == 1:
        return 12
    if a == 1 and b == 1:
        return 8
    if a == 0 or b == 0:
        return 10
    if a - 1 == b or b - 1 == a:
        return 12
    if a == b:
        return 4
    return 8


line = input()
charMap = dict()

for character in line:
    if character.isupper():
        incrementKey(charMap, "shift")
    incrementKey(charMap, character.lower())

charCounts = [(key, charMap[key]) for key in charMap]
charCounts.sort(key = lambda tuple: tuple[1], reverse = True)

dist = 0
a = 0
b = 0
keys = 0
total = 0
maxLen = 0
possibilities = [(0, 0)]

for (word, count) in charCounts:
    if keys == 0:
        (a, b) = possibilities.pop()
        dist = math.hypot(a, b)
        keys = numKeys(a, b)

        if a >= maxLen:
            maxLen = maxLen + 1
            for i in range(maxLen + 1):
                possibilities.append((maxLen, i))

            possibilities.sort(key = lambda tuple: math.hypot(tuple[0], tuple[1]), reverse = True)



    total = total + (count * math.hypot(a, b))
    keys = keys - 1

# Multiply by 2 to include cost of going back to home row
print(round(total * 2, 3))
