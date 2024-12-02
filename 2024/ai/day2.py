def read_input():
    with open('../input/day2.txt', 'r', encoding='utf-8') as f:
        return [list(map(int, line.split())) for line in f]


def is_safe(levels):
    increasing = all(b > a and 1 <= b - a <= 3 for a, b in zip(levels, levels[1:]))
    decreasing = all(b < a and 1 <= a - b <= 3 for a, b in zip(levels, levels[1:]))
    return increasing or decreasing


def can_be_made_safe(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        if is_safe(new_levels):
            return True
    return False


def count_safe_reports(reports, allow_removal=False):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
        elif allow_removal and can_be_made_safe(report):
            count += 1
    return count


def main():
    reports = read_input()

    # Part 1
    safe_count = count_safe_reports(reports)
    print(f"Part 1: {safe_count}")

    # Part 2
    safe_count_with_removal = count_safe_reports(reports, allow_removal=True)
    print(f"Part 2: {safe_count_with_removal}")


if __name__ == "__main__":
    main()
