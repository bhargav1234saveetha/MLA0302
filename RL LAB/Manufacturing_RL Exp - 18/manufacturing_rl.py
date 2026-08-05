import os
import pandas as pd
import numpy as np

# ==========================
# Read CSV File
# ==========================

folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "manufacturing_process.csv")

data = pd.read_csv(csv_file)

print("===== MANUFACTURING DATA =====")
print(data)

# ==========================
# Reward = Product Quality
# ==========================

rewards = data["Quality"].values

gamma = 0.9

value = np.zeros(len(rewards))

# ==========================
# Bellman Value Function
# ==========================

for iteration in range(30):

    new_value = value.copy()

    for i in range(len(rewards)):

        reward = rewards[i]

        if i < len(rewards)-1:

            new_value[i] = reward + gamma * value[i+1]

        else:

            new_value[i] = reward

    value = new_value

# ==========================
# Policy
# ==========================

policy = []

for i in range(len(value)):

    if value[i] >= 95:

        policy.append("Increase Settings")

    elif value[i] >= 92:

        policy.append("Maintain Settings")

    else:

        policy.append("Decrease Settings")

# ==========================
# Results
# ==========================

print("\n===== STATE VALUE FUNCTION =====")

for i in range(len(value)):

    print("Machine :", data["MachineID"][i],
          "Value =", round(value[i],2))

print("\n===== OPTIMAL POLICY =====")

for i in range(len(policy)):

    print(data["MachineID"][i], "->", policy[i])

best = np.argmax(value)

print("\nBest Machine Setting")

print("Machine ID :", data["MachineID"][best])

print("Temperature :", data["Temperature"][best])

print("Pressure :", data["Pressure"][best])

print("Speed :", data["Speed"][best])

print("Quality :", data["Quality"][best])

print("\nExperiment Completed Successfully")
