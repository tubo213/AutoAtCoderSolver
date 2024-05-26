def process_balls(N, A):
    stack = []
    for ai in A:
        while stack and stack[-1] == ai:
            ai = stack.pop() + 1
        stack.append(ai)
    return len(stack)


if __name__ == "__main__":
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    A = list(map(int, data[1:]))

    result = process_balls(N, A)
    print(result)
