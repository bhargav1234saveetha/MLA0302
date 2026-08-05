import os
import pandas as pd
import numpy as np

# ==========================
# Load CSV File
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "robot_navigation.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== ROBOT NAVIGATION GRID =====")
for row in grid:
    print(" ".join(row))

rows = len(grid)
cols = len(grid[0])

# Reward Function
reward = {
    "S": 0,
    ".": -1,
    "T": 5,
    "X": -10,
    "G": 20
}

gamma = 0.9

# Actions
actions = [(-1,0),(1,0),(0,-1),(0,1)]
action_name = ["UP","DOWN","LEFT","RIGHT"]

# Value Function
V = np.zeros((rows, cols))

# ==========================
# Bellman Optimality Update
# ==========================
for iteration in range(25):

    newV = np.copy(V)

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == "X":
                continue

            values = []

            for dx,dy in actions:

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols:

                    r = reward[grid[ni][nj]]

                    values.append(r + gamma * V[ni][nj])

            if values:
                newV[i][j] = max(values)

    V = newV

print("\n===== STATE VALUE FUNCTION =====")
print(np.round(V,2))

# ==========================
# Optimal Path
# ==========================
print("\n===== OPTIMAL POLICY =====")

for i in range(rows):

    for j in range(cols):

        if grid[i][j] == "X":
            print(" X ", end=" ")

        elif grid[i][j] == "G":
            print(" G ", end=" ")

        else:

            best = -99999
            move = ""

            for k,(dx,dy) in enumerate(actions):

                ni = i + dx
                nj = j + dy

                if 0 <= ni < rows and 0 <= nj < cols:

                    if V[ni][nj] > best:
                        best = V[ni][nj]
                        move = action_name[k][0]

            print(move, end="  ")

    print()

print("\nOptimal Path Computed Successfully")
