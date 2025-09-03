import random
import string
import time
from collections.abc import Generator


def random_letter() -> Generator[str, None, None]:
    while True:
        yield random.choice(string.printable)



def string_gen_as_list(string_match: str) -> Generator[list[str], None, str]:
    letter_gen = random_letter()

    while True:
        yield [next(letter_gen) for _ in range(len(string_match))]


def rand_until_match(string_match: str):


    original_string_length = len(string_match)
    original_string_match = string_match

    string_match: list[str] = list(string_match)

    locked_letters: list[str] = []
    current_index: int = 0

    strings: list[str] = []

    while len(locked_letters) != original_string_length:
        string_generator: Generator[list[str], None, str] = string_gen_as_list(''.join(string_match))

        current_jumble: list[str] = next(string_generator)


        try:
            while current_jumble[current_index] != original_string_match[current_index]:
                current_jumble: list[str] = next(string_generator)

                if current_jumble[current_index] == original_string_match[current_index]:

                    locked_letters.append(string_match.pop(current_index))

                yield f'{''.join(locked_letters)}{''.join(current_jumble)}'


        except IndexError:
            break


    return strings



def main():
    string_match = "Searching for fucks: "


    for v in rand_until_match(string_match):
        print(f'{str(v).ljust(5, ' ') + str(random.randint(0, 1000)).center(5, ' ')}', flush=True)
        time.sleep(0.002)

        print('\n'*80, flush=True)

    print('\n'*80, flush=True)

    n = random.randint(0, 1000)

    while n != 0:
        print(f'{string_match}{n}', flush=True)

        n = random.randint(0, 100)

        time.sleep(0.02)
        print('\n'*80, flush=True)

    print(f'{string_match}{n}', flush=True)
    print("No fucks found to give")
    input()

if __name__ == '__main__':
    main()