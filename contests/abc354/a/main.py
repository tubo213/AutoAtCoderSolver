def find_first_day(H):
    day = 0
    height = 0  # Initial height pre-germination

    while height <= H:
        height = (1 << (day + 1)) - 1  # equivalent to 2^(day + 1) - 1
        day += 1

    return day


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    H = int(input().strip())
    print(find_first_day(H))
