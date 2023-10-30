voters = int(input())
votes = dict()

for i in range(voters):
    line = input().split(',')
    for el in line:
        if el in votes:
            votes[el] = votes[el] + 1
        else:
            votes[el] = 1

winningDino = ""
winningVotes = -1
for dino in votes:
    if votes[dino] > winningVotes:
        winningDino = dino
        winningVotes = votes[dino]

print(winningDino)
print(winningVotes)