import os
import pandas as pd
import numpy as np
import random

# ==========================
# Load CSV Dataset
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "pacman_grid.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== PAC-MAN GRID =====")
for row in grid:
    print(" ".join(row))

rows = len(grid)
cols = len(grid[0])

# ==========================
# Rewards
# ==========================
reward = {
    "S": 0,
    ".": -1,
    "F": 5,
    "G": -10,
    "X": -5,
    "T": 20
}

# Actions
actions = ["UP", "DOWN", "LEFT", "RIGHT"]
moves = [(-1,0), (1,0), (0,-1), (0,1)]

# Q-Table
Q = np.zeros((rows, cols, 4))

# Parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 200

# ==========================
# Find Start Position
# ==========================
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            start = (i, j)

# ==========================
# Q-Learning Training
# ==========================
print("\n===== TRAINING =====")

for episode in range(episodes):

    state = start

    while True:

        x, y = state

        # Epsilon-Greedy Action Selection
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(Q[x][y])

        dx, dy = moves[action]

        nx = x + dx
        ny = y + dy

        # Stay inside the grid
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            nx, ny = x, y

        r = reward[grid[nx][ny]]

        # Q-Learning Update
        Q[x][y][action] = Q[x][y][action] + alpha * (
            r + gamma * np.max(Q[nx][ny]) - Q[x][y][action]
        )

        state = (nx, ny)

        # Stop when target is reached
        if grid[nx][ny] == "T":
            break

print("\nTraining Completed Successfully")

# ==========================
# Display Learned Policy
# ==========================
print("\n===== LEARNED POLICY =====")

for i in range(rows):

    for j in range(cols):

        if grid[i][j] == "X":
            print(" X ", end=" ")

        elif grid[i][j] == "T":
            print(" T ", end=" ")

        else:
            best = np.argmax(Q[i][j])
            print(actions[best][0], end="  ")

    print()

# ==========================
# Display Q-Values
# ==========================
print("\n===== Q TABLE =====")

for i in range(rows):
    for j in range(cols):
        print(f"State ({i},{j}) = {Q[i][j]}")
