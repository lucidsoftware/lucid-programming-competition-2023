import math

inputLine = list(map(lambda num: int(num), input().split(' ')))
m = inputLine[0]
n = inputLine[1]

rewardBlock = m * m
cancelBlock = m + m
timesLinear = math.floor(n / cancelBlock)
occurrances = timesLinear * timesLinear
remainder = n % cancelBlock

total = rewardBlock * occurrances

if timesLinear == 0:
    total = total + min(rewardBlock, n * n)
elif remainder >= m:
    total = total + ((timesLinear * 2) + 1) * rewardBlock
else:
    total = total + ((timesLinear * 2)) * m * remainder
    total = total + (remainder * remainder)

print(total, "")