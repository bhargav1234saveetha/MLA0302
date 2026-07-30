gamma = 0.9

grid = [
    ['S', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', 'G']
]

rows = 3
cols = 3

values = [[0 for j in range(cols)] for i in range(rows)]

policy = [['RIGHT' for j in range(cols)] for i in range(rows)]

actions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

changed = True

while changed:

    changed = False

    for _ in range(10):

        new_values = [row[:] for row in values]

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 'X':
                    continue

                reward = 5 if grid[i][j] == 'G' else 0

                move = policy[i][j]

                dx, dy = actions[move]

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != 'X':
                    new_values[i][j] = reward + gamma * values[ni][nj]
                else:
                    new_values[i][j] = reward

        values = new_values

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 'X':
                continue

            best_action = policy[i][j]
            best_value = -999

            for action, (dx, dy) in actions.items():

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] != 'X':

                    if values[ni][nj] > best_value:
                        best_value = values[ni][nj]
                        best_action = action

            if best_action != policy[i][j]:
                policy[i][j] = best_action
                changed = True

print("Optimal Policy\n")

for row in policy:
    print(row)

print("\nValue Function\n")

for row in values:
    print(["%.2f" % v for v in row])
