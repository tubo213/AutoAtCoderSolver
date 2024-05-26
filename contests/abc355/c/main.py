def bingo_first_turn(N, T, A):
    # Create track arrays
    row_count = [0] * N
    col_count = [0] * N
    main_diagonal_count = 0
    anti_diagonal_count = 0

    for turn in range(T):
        value = A[turn]
        # Convert value to 0-based row and column index
        row = (value - 1) // N
        col = (value - 1) % N

        # Mark this cell
        row_count[row] += 1
        col_count[col] += 1
        if row == col:
            main_diagonal_count += 1
        if row + col == N - 1:
            anti_diagonal_count += 1

        # Check if any conditions are met for Bingo
        if (
            row_count[row] == N
            or col_count[col] == N
            or main_diagonal_count == N
            or anti_diagonal_count == N
        ):
            return turn + 1

    return -1


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    T = int(data[1])
    A = list(map(int, data[2 : 2 + T]))
    result = bingo_first_turn(N, T, A)
    print(result)
