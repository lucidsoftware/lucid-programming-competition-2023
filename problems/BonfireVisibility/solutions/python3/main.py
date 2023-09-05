bonfire = input().split(' ')

bonfireX = int(bonfire[0])
bonfireY = int(bonfire[1])

dinoCount = int(input())

dinos = set()

def getGCD(a, b):
    return a if b == 0 else getGCD(b, a % b)

for _ in range(dinoCount):
    dino = input().split(' ')
    dinoX = int(dino[0]) - bonfireX
    dinoY = int(dino[1]) - bonfireY

    gcd = abs(getGCD(dinoX, dinoY))

    dinos.add((dinoX // gcd, dinoY // gcd))

print(len(dinos))