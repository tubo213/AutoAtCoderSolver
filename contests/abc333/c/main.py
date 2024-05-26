def main():
    import sys

    input = sys.stdin.read
    N = int(input().strip())

    # Step 1: Generate repunits up to a reasonable length
    repunits = [
        int("1" * i) for i in range(1, 13)
    ]  # 12 is a safe upper limit (i.e., 111...11 (12 ones))

    # Step 2: Generate all sums of exactly three repunits
    sums = set()
    length = len(repunits)
    for i in range(length):
        for j in range(i, length):
            for k in range(j, length):
                sums.add(repunits[i] + repunits[j] + repunits[k])

    # Step 3: Sort the sums and find the N-th smallest
    sorted_sums = sorted(sums)

    # Step 4: Print the N-th smallest sum
    print(sorted_sums[N - 1])


if __name__ == "__main__":
    main()
