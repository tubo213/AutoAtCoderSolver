def determine_minimum_score(n, x, scores):
    total_initial_sum = sum(scores)

    # All possible scores should lie within 0 to 100
    for possible_score in range(101):
        # Compute total score if this score is added
        total_scores = scores + [possible_score]

        # Sort the scores and pick the middle N-1 numbers after removing the smallest and largest
        total_scores_sorted = sorted(total_scores)
        if sum(total_scores_sorted[1 : n - 1]) >= x:
            return possible_score

    return -1


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    X = int(data[1])
    A = list(map(int, data[2:]))

    print(determine_minimum_score(N, X, A))
