from collections import Counter
from typing import List, Tuple


def get_puzzle_input() -> Tuple[List[int], List[int]]:
    with open('../input/day1.txt', 'r', encoding='utf-8') as file:
        first_list, second_list = [], []
        for line in file.read().splitlines():
            parts = line.split('   ')
            first_list.append(int(parts[0]))
            second_list.append(int(parts[1]))
        return first_list, second_list


def part_1(first_list: List[int], second_list: List[int]) -> None:
    first_list.sort()
    second_list.sort()

    total_distance = sum(abs(a - b) for a, b in zip(first_list, second_list))
    print(f"  Part 1: {total_distance}")


def part_2(first_list: List[int], second_list: List[int]) -> None:
    element_count_map = Counter(second_list)
    similarity_score = sum(value * element_count_map[value] for value in first_list)
    print(f"  Part 2: {similarity_score}")


def main():
    print("Day 1")
    first_list, second_list = get_puzzle_input()
    part_1(first_list, second_list)
    part_2(first_list, second_list)


if __name__ == "__main__":
    main()
