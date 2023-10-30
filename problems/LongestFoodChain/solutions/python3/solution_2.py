chains = {}
visited = {}

def parse_line(line):
    predator = line.split(" <- ")[0]
    prey = line.split(" <- ")[1].split(", ")
    chains[predator] = prey


def get_longest_chain():
    for key in chains.keys():
        if key not in visited:
            visited[key] = 1
        for prey in chains[key]:
            if prey in visited:
                visited[prey] = max(visited[prey], visited[key] + 1)
            else:
                visited[prey] = visited[key] + 1


num_chains = int(input())

for i in range(num_chains):
    parse_line(input())

get_longest_chain()
print(max(visited.values()))
