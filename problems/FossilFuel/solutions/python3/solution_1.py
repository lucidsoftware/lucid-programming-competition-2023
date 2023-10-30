from copy import deepcopy
from itertools import combinations

def checkCombinations(nuggets, numKids, targetAmount, foundSubLists):
    if (foundSubLists == numKids):
        return True
    if sum(nuggets) == targetAmount:
        if checkCombinations([], numKids, targetAmount, foundSubLists + 1):
            return True
    combinationsThatSumToTargetAmount = [seq for i in range(len(nuggets)) for seq in combinations(nuggets, i) if sum(seq) == targetAmount]
    for combination in combinationsThatSumToTargetAmount:
        nugs = deepcopy(nuggets)
        for nugget in combination:
            nugs.remove(nugget)
        if checkCombinations(nugs, numKids, targetAmount, foundSubLists + 1):
            return True
    return False

def getMaxAmountToFeedKids(numKids, nuggetSizes, totalFood):
    # Without this check, test case 8 will timeout
    if numKids > len(nuggetSizes):
        return 0
    for targetAmount in range(totalFood // numKids, 0, -1):
        nuggets = deepcopy(nuggetSizes)
        result = checkCombinations(nuggets, numKids, targetAmount, 0)
        if result:
            return targetAmount
    return 0
    
numKids = eval(input())
nuggetSizes = [eval(nugget) for nugget in input().split()]

totalFood = sum(nuggetSizes)
nuggetSizes.sort(reverse=True)

print(getMaxAmountToFeedKids(numKids, nuggetSizes, totalFood))
