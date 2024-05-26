import sys
from functools import lru_cache

# Reading input
input = sys.stdin.read
data = input().split()

N = int(data[0])
cards = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(N)]


# Memoization: Cache results of the dp function
@lru_cache(None)
def dp(mask, turn):
    # mask is a bitmask representing the remaining cards
    if bin(mask).count("1") == 0:
        return 0  # No cards left means no more values can be added

    if turn == 0:  # Takahashi's turn
        best = float("-inf")
        for i in range(N):
            if mask & (1 << i):
                best = max(best, cards[i][0] - dp(mask & ~(1 << i), 1 - turn))
    else:  # Aoki's turn
        best = float("inf")
        for i in range(N):
            if mask & (1 << i):
                best = min(best, cards[i][1] - dp(mask & ~(1 << i), 1 - turn))

    return best


initial_mask = (1 << N) - 1  # All cards are initially available
result = dp(initial_mask, 0)  # Takahashi starts the game

if result > 0:
    print("Takahashi")
else:
    print("Aoki")
