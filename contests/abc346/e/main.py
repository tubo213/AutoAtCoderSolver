def main():
    import sys

    input = sys.stdin.read

    data = input().strip().split()
    idx = 0

    H = int(data[idx])
    idx += 1
    W = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    # Tracking last updates for rows and columns
    row_updates = [-1] * (H + 1)
    row_colors = [0] * (H + 1)
    col_updates = [-1] * (W + 1)
    col_colors = [0] * (W + 1)

    ops = []

    for i in range(M):
        T = int(data[idx])
        idx += 1
        A = int(data[idx])
        idx += 1
        X = int(data[idx])
        idx += 1
        ops.append((T, A, X, i))

    for T, A, X, time in ops:
        if T == 1:
            row_updates[A] = time
            row_colors[A] = X
        elif T == 2:
            col_updates[A] = time
            col_colors[A] = X

    color_count = {}

    # Count cells based on the maximum update time
    for r in range(1, H + 1):
        for c in range(1, W + 1):
            if row_updates[r] > col_updates[c]:
                color = row_colors[r]
            else:
                color = col_colors[c]
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1

    # Prepare the result
    result = []
    result.append(str(len(color_count)))
    for color, count in sorted(color_count.items()):
        result.append(f"{color} {count}")

    print("\n".join(result))


if __name__ == "__main__":
    main()
