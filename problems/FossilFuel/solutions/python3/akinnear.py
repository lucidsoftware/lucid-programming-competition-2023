from copy import deepcopy
from itertools import combinations

def getMaxAmountToFeedKids(numKids, nuggetSizes, totalFood):
    # Without this check, test case 8 will timeout
    if numKids > len(nuggetSizes):
        return 0
    for targetAmount in range(totalFood // numKids, 0, -1):
        nuggets = deepcopy(nuggetSizes)
        foundSubLists = 0
        while (foundSubLists < numKids):
            # All the combinations of sublists that sum to the target amount
            combinationsThatSumToTargetAmount = [seq for i in range(len(nuggets)) for seq in combinations(nuggets, i) if sum(seq) == targetAmount]
            if (len(combinationsThatSumToTargetAmount) > 0):
                for nugget in combinationsThatSumToTargetAmount[0]:
                    nuggets.remove(nugget)
                foundSubLists += 1
            # Need to check the sum of the entire list since the combinations above just work for sublists
            elif sum(nuggets) == targetAmount:
                foundSubLists += 1
            else:
                break
        if (foundSubLists == numKids):
            return targetAmount
    return 0
    
numKids = eval(input())
nuggetSizes = [eval(nugget) for nugget in input().split()]
totalFood = sum(nuggetSizes)
nuggetSizes.sort(reverse=True)

print(getMaxAmountToFeedKids(numKids, nuggetSizes, totalFood))