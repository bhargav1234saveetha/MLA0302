import os
import pandas as pd

# Load CSV
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "warehouse.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== WAREHOUSE GRID =====")
for row in grid:
    print(" ".join(row))

# Find Start Position
start = None

for i in range(5):
    for j in range(5):
        if grid[i][j] == "S":
            start = (i, j)

print("\nStart Position:", start)

# MDP Components
states = [(i, j) for i in range(5) for j in range(5)]
actions = ["UP", "DOWN", "LEFT", "RIGHT"]

# Reward Function
def reward(cell):
    if cell == "P":
        return 2
    elif cell == "X":
        return -2
    elif cell == "G":
        return 5
    else:
        return 0

# Initial Value Function
values = {}
for state in states:
    values[state] = 0

gamma = 0.9

print("\n===== POLICY EVALUATION =====")

# One iteration of policy evaluation
for state in states:

    x, y = state

    cell = grid[x][y]

    r = reward(cell)

    values[state] = r + gamma * values[state]

# Display Value Function
print("\nState\t\tValue")

for state in states:
    print(state, "\t", values[state])

print("\nPolicy Evaluation Completed")
