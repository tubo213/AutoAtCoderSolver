import sys

input = sys.stdin.read


def main():
    data = input().strip().split()
    N = int(data[0])
    points = []

    # Parsing input
    index = 1
    for i in range(N):
        X = int(data[index])
        Y = int(data[index + 1])
        points.append((X, Y))
        index += 2

    results = []

    # Calculating the farthest point for each point
    for i in range(N):
        max_distance_squared = -1
        farthest_point_id = -1
        x1, y1 = points[i]
        for j in range(N):
            if i != j:
                x2, y2 = points[j]
                distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
                if distance_squared > max_distance_squared:
                    max_distance_squared = distance_squared
                    farthest_point_id = j + 1  # +1 because IDs are 1-based

        results.append(farthest_point_id)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
