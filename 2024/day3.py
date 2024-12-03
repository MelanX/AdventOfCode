import re
from typing import Pattern


def part_1(pattern: Pattern, data: str):
    total = 0

    muls = pattern.findall(data)
    for mul in muls:
        a, b = map(int, mul[4:-1].split(','))
        total += a * b

    print(f'Part 1: {total}')


def part_2(pattern: Pattern, data: str):
    total = 0

    parts = data.split('do()')
    for part in parts:
        part = part.split('don\'t()')[0]
        for mul in pattern.findall(part):
            a, b = map(int, mul[4:-1].split(','))
            total += a * b

    print(f'Part 2 {total}')


def main():
    pattern = re.compile("mul\\(\\d{1,3},\\d{1,3}\\)")

    with open('input/day3.txt', 'r', encoding='utf-8') as f:
        data = f.read()

    part_1(pattern, data)
    part_2(pattern, data)


if __name__ == "__main__":
    main()
