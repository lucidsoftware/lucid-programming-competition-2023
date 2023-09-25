from random import randint, sample, seed, shuffle
from typing import List

seed(42)
test_num = 0
MAX_D = 1000000


def get_test_num() -> int:
    global test_num
    test_num += 1
    return test_num - 1


def write(contents: List[str]):
    n = get_test_num()
    print('Writing test {}...'.format(n))
    with open('tests/{}.in'.format(n), 'w+') as f:
        f.write('\n'.join(contents))


def generate(n: int, c=None, max_d=None):
    test = []
    c = c if c is not None else randint(1, n * (n-1) // 2)
    test.append(f'{n} {c}')
    
    d = max_d or MAX_D
    test.append(' '.join([str(randint(1, d)) for _ in range(n)]))

    # To guarantee we generate a logically consistent input, first generate a pseudo-topological ordering
    # And then generate some edges
    order = list(range(n))
    shuffle(order)
    for _ in range(c):
        x_i, y_i = sample(range(n), 2)
        z = 1 if x_i < y_i else 2
        test.append(f'{order[x_i]} {order[y_i]} {z}')

    write(test)


def examples():
    write(['2 1', '9 5', '0 1 1'])
    write(['3 1', '3 10 5', '0 2 1'])
    write(['3 2', '5 3 3', '2 1 2', '0 2 1'])


def smol():
    generate(1, 0, 1)
    generate(2, 1, 1)


def simple():
    generate(10, 3, 10)
    generate(20, 10, 10)
    generate(50, 20, 10)


def small_duration():
    generate(100, max_d=100)
    generate(500, max_d=100)
    generate(1000, max_d=100)


def maxed():
    generate(1000)
    generate(1000)
    generate(1000)


if __name__ == '__main__':
    examples()
    smol()
    simple()
    small_duration()
    maxed()
