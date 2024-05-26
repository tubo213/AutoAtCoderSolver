def main():
    import sys

    input = sys.stdin.read
    N = int(input().strip())

    # Base pattern
    pattern = "ooxooxoox"

    # Create the result string of length N
    result = (pattern * ((N // len(pattern)) + 1))[:N]

    print(result)


if __name__ == "__main__":
    main()
