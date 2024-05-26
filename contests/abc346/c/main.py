def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2 : 2 + N]))

    # Create a set of elements in A for O(1) look-up time
    A_set = set(A)

    # Sum of the first K natural numbers
    total_sum = K * (K + 1) // 2

    # Calculate the sum of the elements in A that are <= K
    A_sum = 0
    for num in A_set:
        if num <= K:
            A_sum += num

    # The required answer
    result = total_sum - A_sum

    # Output the result
    print(result)


# To run the main function
if __name__ == "__main__":
    main()
