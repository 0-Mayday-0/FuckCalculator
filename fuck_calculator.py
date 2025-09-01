import subprocess
import random
import string
import time
from collections.abc import Generator
from icecream import ic

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

                strings.append(f'{''.join(locked_letters)}{''.join(current_jumble[:len(locked_letters)-1])}')

                if current_jumble[current_index] == original_string_match[current_index]:

                    locked_letters.append(string_match.pop(current_index))
                else:
                    continue


        except IndexError:
            break

        strings.append(f'{''.join(locked_letters)}')

    return strings



def main():
    strings = rand_until_match("Searching for fucks: ")

    for i, v in enumerate(strings):
        print(f'{str(v).ljust(5, ' ') + str(random.randint(0, 1000)).center(5, ' ')}', flush=True)
        time.sleep(0.002)

        if i % 2 == 0:
            subprocess.call("cmd /c cls")

    subprocess.call("cmd /c cls")

    n = random.randint(0, 1000)

    while n != 0:
        print(f'{strings[-1].ljust(5, ' ') + str(n).center(5, ' ')}', flush=True)

        n = random.randint(0, 100)

        time.sleep(0.02)
        subprocess.call("cmd /c cls")

    print(f'{strings[-1].ljust(5, ' ') + str(n).center(5, ' ')}', flush=True)
    print("No fucks found to give")
    input()

if __name__ == '__main__':
    main()