import heapq


def count_intersecting_intervals(intervals):
    # Sort intervals by start point
    intervals.sort()

    # Min-heap to maintain end points of active intervals
    heap = []
    intersect_count = 0

    for interval in intervals:
        start, end = interval
        # Remove intervals from heap that do not overlap with the current interval
        while heap and heap[0] < start:
            heapq.heappop(heap)
        # All remaining intervals in the heap are intersecting with the current interval
        intersect_count += len(heap)
        # Add the current interval's end to the heap
        heapq.heappush(heap, end)

    return intersect_count


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    intervals = []

    for i in range(N):
        l_i = int(data[2 * i + 1])
        r_i = int(data[2 * i + 2])
        intervals.append((l_i, r_i))

    result = count_intersecting_intervals(intervals)
    print(result)


if __name__ == "__main__":
    main()
