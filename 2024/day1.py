def get_data():
    with open('input/day1.txt', 'r', encoding='utf-8') as f:
        left = []
        right = []
        for line in f.read().splitlines():
            parts = line.split('   ')
            left.append(int(parts[0]))
            right.append(int(parts[1]))

        return left, right


def part_1(left, right):
    left.sort()
    right.sort()

    total_distance = 0
    for value_a, value_b in zip(left, right):
        total_distance += abs(value_a - value_b)

    print(f"  Part 1: {total_distance}")


def part_2(left, right):
    already_checked = {}
    similarity_score = 0
    for value in left:
        if value in already_checked:
            similarity_score += already_checked[str(value)]
            continue

        total = 0
        for check in right:
            if value == check:
                total += check

        similarity_score += total
        already_checked[str(value)] = total

    print(f"  Part 2: {similarity_score}")


if __name__ == "__main__":
    print("Day 1")
    left, right = get_data()
    part_1(left, right)
    part_2(left, right)
