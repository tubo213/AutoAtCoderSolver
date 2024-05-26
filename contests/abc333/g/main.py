import sys
import math


def main():
    input_data = sys.stdin.read()
    r, N = map(str.strip, input_data.split())
    r = float(r)
    N = int(N)

    p_best, q_best = 0, 1
    min_diff = abs(r - p_best / q_best)

    for q in range(1, N + 1):
        p = round(r * q)
        if p * q <= N:
            current_diff = abs(r - p / q)
            if current_diff < min_diff:
                p_best, q_best = p, q
                min_diff = current_diff

    print(p_best, q_best)


if __name__ == "__main__":
    main()
