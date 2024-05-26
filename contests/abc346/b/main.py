def is_substring_exist(W, B):
    # The infinite string repetition
    base_string = "wbwbwwbwbwbw"
    period_length = len(base_string)

    # Length of the desired substring
    max_length = W + B

    # Repeat the string enough times to cover all possible substrings of length W + B
    repeated_string = (base_string * ((max_length // period_length) + 2))[
        : (max_length + period_length * 2)
    ]

    # Check all possible substrings of length W + B
    for i in range(len(repeated_string) - max_length + 1):
        substring = repeated_string[i : i + max_length]
        if substring.count("w") == W and substring.count("b") == B:
            return "Yes"

    return "No"


def main():
    # Read input W and B
    W, B = map(int, input().strip().split())

    # Get the result
    result = is_substring_exist(W, B)

    # Print the result
    print(result)


if __name__ == "__main__":
    main()
