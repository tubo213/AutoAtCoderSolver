def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2:]))

    multiples = []
    for number in A:
        if number % K == 0:
            multiples.append(number // K)

    multiples.sort()

    print(" ".join(map(str, multiples)))


if __name__ == "__main__":
    main()
