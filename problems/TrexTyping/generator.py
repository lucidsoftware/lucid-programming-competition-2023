from random import choices, randint, sample, seed
from string import ascii_lowercase as alphas, ascii_uppercase as ALPHAS, digits

seed(42)
MAX_S = 1000000
SYMBOLS = '%$[]^<>{}/\\()@`~o|#=-*!_+.&,\'"?'
test_num = 0
all_characters = [alphas, ALPHAS, digits, SYMBOLS]
MAX_CHARS = sum([len(char_set) for char_set in all_characters]) + 1


def get_test_num() -> int:
    global test_num
    test_num += 1
    return test_num - 1


def write(contents: str):
    n = get_test_num()
    print('Writing test {}...'.format(n))
    with open('tests/{}.in'.format(n), 'w+') as f:
        f.write(contents)


def generate(n: int, n_unique: int, use_lower=True, use_space=True, use_upper=False, use_digits=False, use_symbols=False) -> str:
    s = []
    used_characters = zip(all_characters, [use_lower, use_upper, use_digits, use_symbols])
    pool = ''.join([char_set for char_set, use in used_characters if use])
    char_set = sample(pool, n_unique - use_space)
    
    while n > 0:
        size = randint(1, min(12, n))
        w = ''.join(choices(char_set, k=size))
        s.append(w)
        n -= size + use_space

    return (' ' if use_space else '').join(s)


def examples():
    write('asdf')
    write('peter piper picked a peck of pickled peppers')
    write('O Romeo, Romeo, wherefore art thou Romeo?')


# tests where the answer should be 0
def smol():
    write('a')
    write('Hi')
    write('A z')
    write('ababcdcd')


# simple tests: just random lowercase letters
def lower():
    write(generate(10, 5, use_space=False))
    write(generate(100, 15, use_space=False))
    write(generate(1000, 26, use_space=False))
    write(generate(MAX_S, 26, use_space=False))


# testing shift: just uppercase letters
def upper():
    write(generate(10, 5, use_lower=False, use_space=False, use_upper=True))
    write(generate(100, 15, use_lower=False, use_space=False, use_upper=True))
    write(generate(1000, 26, use_lower=False, use_space=False, use_upper=True))
    write(generate(MAX_S, 26, use_lower=False, use_space=False, use_upper=True))


# words: mix of lower and upper, with spaces thrown in
def words():
    write(generate(10, 5, use_upper=True))
    write(generate(100, 15, use_upper=True))
    write(generate(1000, 27, use_upper=True))
    write(generate(MAX_S, 27, use_upper=True))


# just numbers and spaces
def numbers():
    write(generate(10, 11, use_lower=False, use_digits=True))
    write(generate(100, 11, use_lower=False, use_digits=True))
    write(generate(1000, 11, use_lower=False, use_digits=True))
    write(generate(MAX_S, 11, use_lower=False, use_digits=True))


# just symbols and spaces (want to make sure that symbols ignore unnecessary shifting)
def symbols():
    num_chars = len(SYMBOLS) + 1
    write(generate(10, num_chars, use_lower=False, use_symbols=True))
    write(generate(100, num_chars, use_lower=False, use_symbols=True))
    write(generate(1000, num_chars, use_lower=False, use_symbols=True))
    write(generate(MAX_S, num_chars, use_lower=False, use_symbols=True))


# everything: should be able to handle a mix of anything at this point
def everything():
    write(generate(10, MAX_CHARS, use_upper=True, use_digits=True, use_symbols=True))
    write(generate(100, MAX_CHARS, use_upper=True, use_digits=True, use_symbols=True))
    write(generate(1000, MAX_CHARS, use_upper=True, use_digits=True, use_symbols=True))
    write(generate(MAX_S, MAX_CHARS, use_upper=True, use_digits=True, use_symbols=True))


if __name__ == '__main__':
    examples()
    smol()
    lower()
    upper()
    words()
    numbers()
    symbols()
    everything()
