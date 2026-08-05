import os
import pandas as pd
import numpy as np

# Read CSV
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "drone_grid.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== CITY GRID =====")

for row in grid:
    print(" ".join(row))

# Rewards
reward = {
    ".":0,
    "S":0,
    "X":-2,
    "D1":3,
    "D2":3,
    "D3":3,
    "G":5
}

rows = 5
cols = 5

gamma = 0.9

# Initial Values
V = np.zeros((rows, cols))

print("\nInitial Value Function\n")
print(V)

# Policy Evaluation
for iteration in range(10):

    newV = np.copy(V)

    for i in range(rows):
        for j in range(cols):

            cell = grid[i][j]

            newV[i][j] = reward[cell] + gamma*V[i][j]

    V = newV

print("\n===== FINAL VALUE FUNCTION =====")
print(V)

print("\nPolicy Iteration Completed Successfully")
