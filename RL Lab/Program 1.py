import random

grid = [
    ['S', '.', 'D', '.', '.'],
    ['.', 'X', '.', 'D', '.'],
    ['.', '.', '.', 'X', '.'],
    ['D', '.', '.', '.', '.'],
    ['.', 'X', '.', 'D', '.']
]

row = 0
col = 0
reward = 0

for i in range(20):

    move = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    if move == "UP" and row > 0:
        row -= 1
    elif move == "DOWN" and row < 4:
        row += 1
    elif move == "LEFT" and col > 0:
        col -= 1
    elif move == "RIGHT" and col < 4:
        col += 1

    print("Move:", move)
    print("Position:", (row, col))

    if grid[row][col] == "D":
        reward += 1
        print("Cleaned Dirt (+1)")
        grid[row][col] = '.'

    elif grid[row][col] == "X":
        reward -= 1
        print("Hit Obstacle (-1)")

    print("Total Reward:", reward)
    print()

print("Final Reward =", reward)
