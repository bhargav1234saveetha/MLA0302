import os
import pandas as pd
import random

# Get the folder where robot.py is saved
folder = os.path.dirname(os.path.abspath(__file__))

# Full path of grid.csv
csv_file = os.path.join(folder, "grid.csv")

# Read CSV file
grid = pd.read_csv(csv_file, header=None).values

print("===== GRID ENVIRONMENT =====")
for row in grid:
    print(" ".join(row))

# Find Start Position
start = None
for i in range(5):
    for j in range(5):
        if grid[i][j] == "S":
            start = (i, j)

print("\nStart Position:", start)

# Actions
actions = ["UP", "DOWN", "LEFT", "RIGHT"]

# Reward Function
def get_reward(cell):
    if cell == "D":
        return 1
    elif cell == "X":
        return -1
    elif cell == "G":
        return 5
    else:
        return 0

# Random Policy
position = start
total_reward = 0

print("\n===== RANDOM POLICY =====")

for step in range(10):

    move = random.choice(actions)

    x, y = position

    if move == "UP" and x > 0:
        x -= 1
    elif move == "DOWN" and x < 4:
        x += 1
    elif move == "LEFT" and y > 0:
        y -= 1
    elif move == "RIGHT" and y < 4:
        y += 1

    position = (x, y)

    reward = get_reward(grid[x][y])
    total_reward += reward

    print(move, "->", position, "Reward =", reward)

print("\nTotal Reward =", total_reward)
