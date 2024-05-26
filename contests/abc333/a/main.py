def main():
    import sys

    input = sys.stdin.read

    # Read input N
    N = int(input().strip())

    # Generate the repeated string
    result = str(N) * N

    # Print the result
    print(result)


if __name__ == "__main__":
    main()
