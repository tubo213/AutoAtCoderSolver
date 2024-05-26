def find_culprit(A, B):
    # If both memories are the same, culprit can't be identified
    if A == B:
        return -1

    # Sum of suspects is 1 + 2 + 3 = 6, third person is 6 - (A + B)
    total_sum_of_suspects = 6
    culprit = total_sum_of_suspects - (A + B)

    return culprit


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    # Reading input
    A, B = map(int, input().split())
    # Find and print the culprit
    result = find_culprit(A, B)
    print(result)
