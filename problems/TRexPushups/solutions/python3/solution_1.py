n = eval(input())
terrain = [eval(elevation) for elevation in input().split()]

count = 0
for i in range(n-1):
    if (terrain[i] - terrain[i+1] >= 4):
        count += 1
print(count)