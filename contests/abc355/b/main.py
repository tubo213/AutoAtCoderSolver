def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    M = int(data[1])
    A = list(map(int, data[2 : 2 + N]))
    B = list(map(int, data[2 + N :]))

    # Merge and sort the array
    C = sorted(A + B)

    # Convert A to a set for quick lookups
    A_set = set(A)

    # Check for consecutive elements in the sorted C that are both in A
    for i in range(1, len(C)):
        if C[i] in A_set and C[i - 1] in A_set:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
