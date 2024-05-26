def main():
    import sys

    input = sys.stdin.read

    data = input().split()
    A = list(map(int, data[:9]))
    B = list(map(int, data[9:]))

    # Total runs scored by each team over the first 8 innings
    total_A = sum(A)
    total_B = sum(B)

    # Determine the number of runs Aoki needs.
    runs_needed = (total_A - total_B) + 1

    # Output the result
    print(max(runs_needed, 1))


if __name__ == "__main__":
    main()
