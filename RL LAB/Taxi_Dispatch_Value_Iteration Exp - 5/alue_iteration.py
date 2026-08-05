import os
import pandas as pd
import numpy as np

# ===========================
# Read CSV File
# ===========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "taxi_dispatch.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== TAXI DISPATCH GRID =====")
for row in grid:
    print(" ".join(row))

# ===========================
# Reward Table
# ===========================
reward = {
    "S": 0,
    ".": 0,
    "P1": 3,
    "P2": 3,
    "X": -2,
    "G": 5
}

rows = 5
cols = 5
gamma = 0.9

# Initialize Value Function
V = np.zeros((rows, cols))

# Actions
actions = [(-1,0),(1,0),(0,-1),(0,1)]   # Up, Down, Left, Right

# ===========================
# Value Iteration
# ===========================
for iteration in range(20):

    newV = np.copy(V)

    for i in range(rows):
        for j in range(cols):

            values = []

            for dx, dy in actions:

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols:

                    cell = grid[ni][nj]

                    r = reward[cell]

                    values.append(r + gamma * V[ni][nj])

            if values:
                newV[i][j] = max(values)

    V = newV

# ===========================
# Print Value Function
# ===========================
print("\n===== VALUE FUNCTION =====")

for row in V:
    print(["{:.2f}".format(x) for x in row])

# ===========================
# Optimal Policy
# ===========================
policy = np.full((rows, cols), " ")

symbols = {
    (-1,0): "↑",
    (1,0): "↓",
    (0,-1): "←",
    (0,1): "→"
}

for i in range(rows):
    for j in range(cols):

        best_value = -9999
        best_action = " "

        for dx, dy in actions:

            ni = i + dx
            nj = j + dy

            if 0 <= ni < rows and 0 <= nj < cols:

                if V[ni][nj] > best_value:

                    best_value = V[ni][nj]
                    best_action = symbols[(dx,dy)]

        policy[i][j] = best_action

print("\n===== OPTIMAL POLICY =====")

for row in policy:
    print(" ".join(row))

print("\nOptimal Dispatch Policy Found Successfully!")
