import math
(n, d, s) = map(lambda x: int(x), input().split())

plots = []
for i in range(n):
    plots.append(int(input()))

plots.sort(reverse = True)

rollingSum = sum(plots[d:])
startingIndex = 0

while rollingSum < s:
    rollingSum = rollingSum + plots[startingIndex] - plots[d + startingIndex]
    startingIndex = startingIndex + 1

minDiff = math.inf
for i in range(startingIndex, n - d + 1):
    diff = plots[i] - plots[i + d - 1]
    minDiff = min(diff, minDiff)

print(minDiff)