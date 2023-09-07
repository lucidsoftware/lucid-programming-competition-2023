from collections import Counter

num_responses = int(input())
responses = [input() for i in range(num_responses)]
dinosaurs = [dinosaur for response in responses for dinosaur in response.split(',')]
beloved_dinosaur = Counter(dinosaurs).most_common(1)[0]
print(beloved_dinosaur[0])
print(beloved_dinosaur[1])
