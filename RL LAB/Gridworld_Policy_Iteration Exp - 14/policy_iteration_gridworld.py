import os
import pandas as pd
import numpy as np

# ==========================
# Load CSV Dataset
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "gridworld_dp.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== GRID WORLD =====")
for row in grid:
    print(" ".join(row))

rows = len(grid)
cols = len(grid[0])

# ==========================
# Reward Function
# ==========================
reward = {
    "S": 0,
    ".": -1,
    "X": -10,
    "G": 20
}

# Actions
actions = [(-1,0), (1,0), (0,-1), (0,1)]
action_name = ["UP", "DOWN", "LEFT", "RIGHT"]

gamma = 0.9

# Initialize Value Function
V = np.zeros((rows, cols))

# Initial Policy (All UP)
policy = np.zeros((rows, cols), dtype=int)

# ==========================
# Policy Iteration
# ==========================
stable = False

while not stable:

    # ----------------------
    # Policy Evaluation
    # ----------------------
    for _ in range(20):

        newV = np.copy(V)

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "X" or grid[i][j] == "G":
                    continue

                action = policy[i][j]

                dx, dy = actions[action]

                ni = max(0, min(rows-1, i+dx))
                nj = max(0, min(cols-1, j+dy))

                r = reward[grid[ni][nj]]

                newV[i][j] = r + gamma * V[ni][nj]

        V = newV

    # ----------------------
    # Policy Improvement
    # ----------------------
    stable = True

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == "X" or grid[i][j] == "G":
                continue

            old_action = policy[i][j]

            values = []

            for dx, dy in actions:

                ni = max(0, min(rows-1, i+dx))
                nj = max(0, min(cols-1, j+dy))

                r = reward[grid[ni][nj]]

                values.append(r + gamma * V[ni][nj])

            best_action = np.argmax(values)

            policy[i][j] = best_action

            if best_action != old_action:
                stable = False

# ==========================
# Display Value Function
# ==========================
print("\n===== VALUE FUNCTION =====")
print(np.round(V,2))

# ==========================
# Display Optimal Policy
# ==========================
print("\n===== OPTIMAL POLICY =====")

for i in range(rows):

    for j in range(cols):

        if grid[i][j] == "X":
            print(" X ", end=" ")

        elif grid[i][j] == "G":
            print(" G ", end=" ")

        else:
            print(action_name[policy[i][j]][0], end="  ")

    print()

print("\nPolicy Iteration Completed Successfully")
