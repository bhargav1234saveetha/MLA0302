import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "delivery_robot.csv")

grid = pd.read_csv(csv_file, header=None).values

print("===== DELIVERY ROBOT GRID =====")

for row in grid:
    print(" ".join(row))

# Rewards
reward = {
    "S":0,
    ".":0,
    "D1":3,
    "D2":3,
    "D3":3,
    "X":-2,
    "G":5
}

rows = 5
cols = 5

gamma = 0.9

# Initial Value Function
V = np.zeros((rows, cols))

actions = [(-1,0),(1,0),(0,-1),(0,1)]

# Bellman Equation
for iteration in range(20):

    newV = np.copy(V)

    for i in range(rows):
        for j in range(cols):

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

print(V)

# Visualize Value Function
plt.imshow(V, cmap="viridis")
plt.colorbar(label="State Value")

for i in range(rows):
    for j in range(cols):
        plt.text(j, i, f"{V[i,j]:.1f}",
                 ha="center",
                 color="white")

plt.title("State Value Function")
plt.show()
