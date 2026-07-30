grid = [
    ['S', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', 'G']
]

row = 0
col = 0
steps = 0

print("Path Followed:\n")

while (row, col) != (2, 2):

    print((row, col))

    if col < 2 and grid[row][col + 1] != 'X':
        col += 1

    elif row < 2 and grid[row + 1][col] != 'X':
        row += 1

    else:
        break

    steps += 1

print((row, col))

if (row, col) == (2, 2):
    print("\nDestination Reached")
else:
    print("\nDestination Not Reached")

print("Total Steps =", steps)
