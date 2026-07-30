gamma = 0.9

grid = [
    ['S', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', 'P']
]

rows = 3
cols = 3

values = [[0 for j in range(cols)] for i in range(rows)]

actions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

for k in range(20):

    new_values = [row[:] for row in values]

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 'X':
                continue

            reward = 0

            if grid[i][j] == 'P':
                reward = 10

            best = -999

            for dx, dy in actions.values():

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols:

                    if grid[ni][nj] != 'X':

                        value = reward + gamma * values[ni][nj]

                        if value > best:
                            best = value

            new_values[i][j] = best

    values = new_values

policy = [["" for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):

        if grid[i][j] == 'X':
            policy[i][j] = "X"
            continue

        best = -999
        move = ""

        for action, (dx, dy) in actions.items():

            ni = i + dx
            nj = j + dy

            if 0 <= ni < rows and 0 <= nj < cols:

                if grid[ni][nj] != 'X':

                    if values[ni][nj] > best:
                        best = values[ni][nj]
                        move = action

        policy[i][j] = move

print("Value Function\n")

for row in values:
    print(["%.2f" % v for v in row])

print("\nOptimal Policy\n")

for row in policy:
    print(row)
