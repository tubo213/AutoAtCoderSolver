def main():
    import sys

    input = sys.stdin.read

    # Read input values
    data = input().strip().split()
    S1S2 = data[0]
    T1T2 = data[1]

    # Map each vertex label to an index
    index_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    # Extract the points from the input
    S1, S2 = S1S2[0], S1S2[1]
    T1, T2 = T1T2[0], T1T2[1]

    # Get corresponding indices
    S1_idx = index_map[S1]
    S2_idx = index_map[S2]
    T1_idx = index_map[T1]
    T2_idx = index_map[T2]

    # Function to calculate distance in terms of steps in the pentagon
    def distance(idx1, idx2):
        return min((idx1 - idx2) % 5, (idx2 - idx1) % 5)

    # Calculate the steps-difference for the two segments
    S_distance = distance(S1_idx, S2_idx)
    T_distance = distance(T1_idx, T2_idx)

    # Check if the distances are equal
    if S_distance == T_distance:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
