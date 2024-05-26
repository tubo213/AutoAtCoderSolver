def find_differing_cell(N, gridA, gridB):
    for i in range(N):
        for j in range(N):
            if gridA[i][j] != gridB[i][j]:
                return i + 1, j + 1  # converting 0-indexed to 1-indexed


# Reading input
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
gridA = []
gridB = []

index = 1
for _ in range(N):
    gridA.append(data[index])
    index += 1

for _ in range(N):
    gridB.append(data[index])
    index += 1

i, j = find_differing_cell(N, gridA, gridB)
print(i, j)
