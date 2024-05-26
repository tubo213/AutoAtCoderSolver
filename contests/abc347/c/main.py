def main():
    import sys

    input = sys.stdin.read
    data = list(map(int, input().split()))

    N = data[0]
    A = data[1]
    B = data[2]
    plans = data[3:]

    total_days = A + B

    for day in plans:
        if (day % total_days > 0) and (day % total_days <= A):
            continue
        else:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
