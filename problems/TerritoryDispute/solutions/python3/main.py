#read input
count, dinos, public_need = map(int, input().split(' '))
territories = [int(input()) for _ in range(count)]

#sort list for sliding window
territories.sort()

#get total land size at every sorted index
total_land = 0
territories_sum = [0]
for i in range(count):
    total_land += territories[i]
    territories_sum.append(total_land)

best = -1
#find best territory with a sliding window
for i in range(count-dinos+1):
    #subtract potential land used by dinos from the total to check viability
    available_land = total_land - territories_sum[i+dinos] + territories_sum[i]
    if (available_land >= public_need):
        #find the difference and compare it to previous best
        diff = territories[i+dinos-1] - territories[i]
        if  diff < best or best == -1:
            best = diff

print(best)