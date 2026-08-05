import os
import pandas as pd
import random

# ==========================
# Load Dataset
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "call_center.csv")

data = pd.read_csv(csv_file)

print("===== CALL CENTER DATA =====")
print(data)

episodes = 100
gamma = 0.9

value = 0

print("\n===== MONTE CARLO SIMULATION =====")

for episode in range(episodes):

    total_reward = 0

    # Random assignment policy
    row = data.sample().iloc[0]

    service_time = row["ServiceTime"]
    resolved = row["Resolved"]

    # Reward
    reward = 10 if resolved == 1 else -5
    reward -= service_time

    total_reward += reward

    # Monte Carlo Value Update
    value = value + (total_reward - value) / (episode + 1)

print("\nEstimated State Value =", round(value, 2))

# Compare Two Policies
print("\n===== POLICY COMPARISON =====")

random_policy = value

best_policy = data[data["Resolved"] == 1]
best_reward = ((10 - best_policy["ServiceTime"]).mean())

print("Random Assignment Value :", round(random_policy, 2))
print("Best Representative Policy :", round(best_reward, 2))

if best_reward > random_policy:
    print("\nBest Policy : Assign calls to representatives with higher resolution rate.")
else:
    print("\nBest Policy : Random Assignment")

print("\nExperiment Completed Successfully")
