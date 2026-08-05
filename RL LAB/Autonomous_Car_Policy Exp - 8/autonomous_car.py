import os
import pandas as pd
import random

# ==========================
# Load CSV File
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "autonomous_car_road.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== ROAD NETWORK =====")
for row in grid:
    print(" ".join(row))

rows = len(grid)
cols = len(grid[0])

# ==========================
# Find Start and Goal
# ==========================
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "G":
            goal = (i, j)

print("\nStart :", start)
print("Goal  :", goal)

# ==========================
# Reward Function
# ==========================
def reward(cell):
    if cell == "G":
        return 5
    elif cell == "X":
        return -5
    elif cell == "I":
        return 1
    else:
        return 0

# ==========================
# RANDOM POLICY
# ==========================
print("\n===== RANDOM POLICY =====")

position = start
total_reward = 0

actions = ["UP","DOWN","LEFT","RIGHT"]

for step in range(15):

    move = random.choice(actions)

    x, y = position

    if move == "UP" and x > 0:
        x -= 1
    elif move == "DOWN" and x < rows-1:
        x += 1
    elif move == "LEFT" and y > 0:
        y -= 1
    elif move == "RIGHT" and y < cols-1:
        y += 1

    position = (x, y)

    r = reward(grid[x][y])
    total_reward += r

    print(move, "->", position, "Reward =", r)

    if position == goal:
        print("Goal Reached!")
        break

print("Random Policy Reward =", total_reward)

# ==========================
# SAFE POLICY
# ==========================
print("\n===== SAFE POLICY =====")

position = start
total_reward = 0
steps = 0

while position != goal and steps < 30:

    x, y = position

    if y < cols-1 and grid[x][y+1] != "X":
        y += 1
        move = "RIGHT"

    elif x < rows-1 and grid[x+1][y] != "X":
        x += 1
        move = "DOWN"

    elif y > 0:
        y -= 1
        move = "LEFT"

    elif x > 0:
        x -= 1
        move = "UP"

    position = (x, y)

    r = reward(grid[x][y])
    total_reward += r

    print(move, "->", position, "Reward =", r)

    steps += 1

print("\nSafe Policy Reward =", total_reward)

if position == goal:
    print("Destination Reached Successfully")
else:
    print("Goal Not Reached")

# ==========================
# Comparison
# ==========================
print("\n===== POLICY COMPARISON =====")

print("Random Policy Reward :", total_reward)

print("Safe Policy completed with", steps, "steps")

print("\nExperiment Completed Successfully")
