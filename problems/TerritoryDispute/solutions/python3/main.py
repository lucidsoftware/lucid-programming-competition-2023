#read input
count, dinos, public_need = map(int, input().split(' '))
territories = [int(input()) for _ in range(count)]

#get total size of land to check viability of specific subsets
total_land = sum(territories)

#sort list for sliding window
territories.sort()
best = -1
#find best territory with a sliding window
for i in range(count-dinos+1):
    #subtract potential land used by dinos from the total to check viability
    available_land = total_land - sum(territories[i:i+dinos])
    if (available_land >= public_need):
        #find the difference and compare it to previous best
        diff = territories[i+dinos-1] - territories[i]
        if  diff < best or best == -1:
            best = diff

print(best)