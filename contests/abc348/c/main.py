import sys
import collections


def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    beans = data[1:]

    # Dictionary to store the minimum deliciousness for each color
    color_map = collections.defaultdict(list)

    for i in range(N):
        A = int(beans[2 * i])
        C = int(beans[2 * i + 1])
        color_map[C].append(A)

    # Find the minimum deliciousness for each color
    min_deliciousness = []
    for color, values in color_map.items():
        min_deliciousness.append(min(values))

    # The answer is the maximum of these minimum deliciousness values
    result = max(min_deliciousness)

    print(result)


if __name__ == "__main__":
    main()
