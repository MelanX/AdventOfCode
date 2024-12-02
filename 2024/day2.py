def get_data():
    with open('input/day2.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            data.append(list(map(int, line.split(' '))))

        return data

def part_1(data):
    counter = 0
    for line in data:
        safe = is_safe(line)
        counter += int(safe)

    print(f"Part 1: {counter}")


def part_2(data):
    counter = 0
    for line in data:
        safe = is_safe(line)
        if not safe:
            for i in range(len(line)):
                copied_line = line.copy()
                del copied_line[i]
                safe = is_safe(copied_line)
                if safe:
                    break

        counter += int(safe)

    print(f"Part 2: {counter}")


def is_safe(levels: list):
    prev = None
    prev_diff = None
    for level in levels:
        if levels.count(level) > 1:
            return False

        if prev is None:
            prev = level
            continue

        diff = prev - level
        if abs(diff) > 3:
            return False

        if prev_diff is None:
            prev = level
            prev_diff = diff
            continue

        if (prev_diff > 0 and diff > 0) or (prev_diff < 0 and diff < 0):
            prev = level
            prev_diff = diff
            continue

        return False

    return True


def main():
    part_1(get_data())
    part_2(get_data())


if __name__ == "__main__":
    main()
