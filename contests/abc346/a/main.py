def main():
    import sys

    input = sys.stdin.read

    # Read and prepare the input data
    input_data = input().strip().split()

    # First value is N, the rest are the values of A
    N = int(input_data[0])
    A = list(map(int, input_data[1:]))

    # Compute the B array
    B = []
    for i in range(N - 1):
        B.append(A[i] * A[i + 1])

    # Print the result
    print(" ".join(map(str, B)))


# Run the main function
if __name__ == "__main__":
    main()
