import re
from typing import Pattern


def calculate_total(pattern: Pattern, data: str, manage_conditions: bool = False) -> int:
    total = 0
    enabled = True

    if manage_conditions:
        # Split on 'do()' and 'don't()', keeping delimiters in the list
        parts = re.split(r"(do\(\)|don't\(\))", data)
    else:
        parts = [data]

    for part in parts:
        if manage_conditions:
            if part == "do()":
                enabled = True
            elif part == "don't()":
                enabled = False
            elif enabled:
                for match in pattern.finditer(part):
                    a, b = map(int, match.groups())
                    total += a * b
        else:
            for match in pattern.finditer(part):
                a, b = map(int, match.groups())
                total += a * b

    return total


def display_results(pattern: Pattern, data: str):
    total_part1 = calculate_total(pattern, data)
    total_part2 = calculate_total(pattern, data, manage_conditions=True)
    print(f'Part 1: {total_part1}')
    print(f'Part 2: {total_part2}')


def main():
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    with open('../input/day3.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    display_results(pattern, data)


if __name__ == "__main__":
    main()
