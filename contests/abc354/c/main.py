def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    # Parsing the input
    N = int(data[0])
    cards = []
    for i in range(N):
        A_i = int(data[2 * i + 1])
        C_i = int(data[2 * i + 2])
        cards.append((A_i, C_i, i + 1))  # (strength, cost, original_index)

    # Sort cards by strength
    cards.sort()

    # Variable to maintain remaining cards
    remaining_cards = []

    min_cost_so_far = float("inf")

    # Traverse the cards in reverse order
    for strength, cost, index in reversed(cards):
        if cost < min_cost_so_far:
            remaining_cards.append(index)
            min_cost_so_far = cost

    # Reversing the remaining cards as we traversed the list in reverse
    remaining_cards.reverse()

    # Output format
    remaining_cards.sort()
    print(len(remaining_cards))
    print(" ".join(map(str, remaining_cards)))


if __name__ == "__main__":
    main()
