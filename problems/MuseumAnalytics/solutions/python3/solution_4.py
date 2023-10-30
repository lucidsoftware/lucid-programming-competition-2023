def most_popular_dinosaur(responses):
    dinosaur_counts = {}
    
    for response in responses:
        dinosaurs = response.split(',')
        for dinosaur in dinosaurs:
            dinosaur = dinosaur.strip()
            if dinosaur in dinosaur_counts:
                dinosaur_counts[dinosaur] += 1
            else:
                dinosaur_counts[dinosaur] = 1
    
    most_popular = max(dinosaur_counts, key=dinosaur_counts.get)
    max_count = dinosaur_counts[most_popular]
    return most_popular, max_count

# Accepting input
responses = []
num_responses = int(input())

for _ in range(num_responses):
    response = input()
    responses.append(response)

popular_dinosaur, max_count = most_popular_dinosaur(responses)
print(f"{popular_dinosaur}\n{max_count}")
