import os
import pandas as pd
import numpy as np
import random

# Load Dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "robot_vacuum.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== HOUSE MAP =====")
for row in grid:
    print(" ".join(row))

rows = len(grid)
cols = len(grid[0])

# Rewards
reward = {
    "S": 0,
    ".": -1,
    "D": 5,
    "X": -5,
    "G": 10
}

actions = ["UP", "DOWN", "LEFT", "RIGHT"]
moves = [(-1,0), (1,0), (0,-1), (0,1)]

Q = np.zeros((rows, cols, 4))

alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 100

# Find Start
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            start = (i, j)

print("\n===== SARSA TRAINING =====")

for ep in range(episodes):

    state = start

    if random.random() < epsilon:
        action = random.randint(0, 3)
    else:
        action = np.argmax(Q[state[0], state[1]])

    while True:

        x, y = state
        dx, dy = moves[action]

        nx = max(0, min(rows - 1, x + dx))
        ny = max(0, min(cols - 1, y + dy))

        r = reward[grid[nx][ny]]

        if random.random() < epsilon:
            next_action = random.randint(0, 3)
        else:
            next_action = np.argmax(Q[nx, ny])

        Q[x, y, action] += alpha * (
            r +
            gamma * Q[nx, ny, next_action] -
            Q[x, y, action]
        )

        state = (nx, ny)
        action = next_action

        if grid[nx][ny] == "G":
            break

print("\n===== LEARNED POLICY =====")

for i in range(rows):
    for j in range(cols):

        if grid[i][j] == "X":
            print(" X ", end=" ")
        else:
            best = np.argmax(Q[i, j])
            print(actions[best][0], end="  ")
    print()

print("\nTraining Completed Successfully")
