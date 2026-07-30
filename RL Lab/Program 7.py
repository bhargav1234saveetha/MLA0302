gamma = 0.9

grid = [
    ['S', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', 'D']
]

rows = 3
cols = 3

values = [[0 for j in range(cols)] for i in range(rows)]

for k in range(20):

    new_values = [row[:] for row in values]

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 'X':
                new_values[i][j] = -1
                continue

            reward = 0

            if grid[i][j] == 'D':
                reward = 10

            best = 0

            actions = [(-1,0),(1,0),(0,-1),(0,1)]

            for dx, dy in actions:

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols:

                    if grid[ni][nj] != 'X':

                        if values[ni][nj] > best:
                            best = values[ni][nj]

            new_values[i][j] = reward + gamma * best

    values = new_values

print("State Value Function\n")

for row in values:
    print(["%.2f" % v for v in row])
