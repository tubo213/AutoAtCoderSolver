def is_321like_number(N):
    N_str = str(N)

    for i in range(1, len(N_str)):
        if not (N_str[i] == N_str[i - 1] or int(N_str[i]) == int(N_str[i - 1]) - 1):
            return "No"

    return "Yes"


# Reading input
if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    N = int(input().strip())
    print(is_321like_number(N))
