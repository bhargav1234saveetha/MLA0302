gamma = 0.9

grid = [
    ['S', '.', 'I'],
    ['.', 'X', '.'],
    ['.', '.', 'G']
]

rows = 3
cols = 3

values = [[0 for j in range(cols)] for i in range(rows)]

for k in range(20):

    new_values = [row[:] for row in values]

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 'X':
                new_values[i][j] = -2
                continue

            reward = 0

            if grid[i][j] == 'I':
                reward = 2
            elif grid[i][j] == 'G':
                reward = 5

            if j < cols - 1 and grid[i][j + 1] != 'X':
                new_values[i][j] = reward + gamma * values[i][j + 1]

            elif i < rows - 1 and grid[i + 1][j] != 'X':
                new_values[i][j] = reward + gamma * values[i + 1][j]

            else:
                new_values[i][j] = reward

    values = new_values

print("Value Function\n")

for row in values:
    print(["%.2f" % v for v in row])
