kids = int(input())
nuggets = list(map(int, input().strip().split(' ')))

total = sum(nuggets)


def checkSize(size: int):
    counts = [0 for _ in range(kids)]
    return recurse(nuggets, counts, size, size * kids, total)

def recurse(remaining: "list[int]", counts: "list[int]", size: int, needed: int, remainingSum: int):
    if len(remaining) == 0:
        return counts.count(size) == len(counts)
    if remainingSum < needed:
        return False

    value = remaining.pop()
    for j in range(len(counts)):
        if counts[j] + value <= size:
            counts[j] += value
            if recurse(remaining.copy(), counts.copy(), size, needed - value, remainingSum - value):
                return True
            counts[j] -= value
    return recurse(remaining, counts, size, needed, remainingSum - value)

if len(nuggets) < kids:
    print(0)
else:
    result = 0
    for i in range((total // kids), 0, -1):
        if checkSize(i):
            result = i
            break
    print(result)
