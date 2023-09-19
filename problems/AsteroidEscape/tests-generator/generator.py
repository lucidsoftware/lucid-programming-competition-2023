import random
import math

def createTestCase(file): 
    randF = 100
    n = random.randint(200, 250)
    m = random.randint(n * 2, math.ceil((n * (n - 1)) / 4))
    f = random.randint(randF * math.ceil(n / 20), randF * math.ceil(n / 5))

    file.write(str(n) + " " + str(m) + " " + str(f) + "\n")

    for i in range(n-1):
        file.write(str(random.randint(0, randF)) + " ")
    file.write(str(random.randint(0, randF)) + "\n")

    edgeSet = set()


    def generateEdge():
        num1 = random.randint(1, n)
        num2 = random.randint(1, n)
        while num1 == num2:
            num2 = random.randint(1, n)
    
        if num1 < num2 and (num1, num2) not in edgeSet:
            edgeSet.add((num1, num2))
            return str(num1) + " " + str(num2)
        elif num2 < num1 and (num2, num1) not in edgeSet:
            edgeSet.add((num1, num2))
            return str(num2) + " " + str(num1)
        else: 
            return generateEdge()

    for j in range(m-1):
        file.write(generateEdge() + "\n")
    file.write(generateEdge())

for i in range(10, 11):
    createTestCase(open(str(i) + ".in", "w"))