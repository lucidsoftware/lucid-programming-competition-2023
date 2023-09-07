import random
import sys

utah_dinos = '''Utahraptorix
Saltlakosaurus
Wasatchceratops
Provopteryx
San Juanosaurus
South Jordan Swiftclaw
Redrockraptor
Juab Canyonwhirl
Vermilionvelociraptor
Escalantespin'''.split('\n')


def check_has_unique_max_value(d):
    max_value = max(d.values())
    count_max_value = sum(1 for value in d.values() if value == max_value)
    return count_max_value == 1

def generate_test_case(num_responses, num_unique_dinos, use_utah_dinos):
    responses = []
    for _ in range(num_responses):
        num_response_dinos = random.randint(1, num_unique_dinos)
        random_dinos = random.sample(utah_dinos, num_response_dinos)
        responses.append(random_dinos)

    beloved_map = {}
    for response in responses:
        for dinosaur in response:
            beloved_map[dinosaur] = beloved_map.get(dinosaur, 0) + 1
    
    print(beloved_map, file=sys.stderr)
    if not check_has_unique_max_value(beloved_map):
        print('Does not have a unique max, regenerating...\n', file=sys.stderr)
        return generate_test_case(num_responses, num_unique_dinos, use_utah_dinos)

    return responses

def format_test_case(responses):
    return "{}\n{}".format(len(responses), '\n'.join([','.join(response) for response in responses]))

print(format_test_case(generate_test_case(random.randint(1, 5), random.randint(1, 10), True)))
