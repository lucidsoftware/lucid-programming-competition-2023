n = eval(input())

favorites = {}
for i in range(n):
    response = input().split()
    for dino in response:
        if dino in favorites:
            favorites[dino] += 1
        else:
            favorites[dino] = 1

sortedFavorites = sorted(favorites.items(), key=lambda x:x[1], reverse=True)
winner = sortedFavorites[0]
print(winner[0])
print(winner[1])