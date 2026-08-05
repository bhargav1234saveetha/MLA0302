import os
import pandas as pd
import numpy as np
import random

# ==========================
# Load Dataset
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "call_center_mc.csv")

data = pd.read_csv(csv_file)

print("===== CALL CENTER DATA =====")
print(data)

representatives = data["Representative"].unique().tolist()

Q = {rep: 0 for rep in representatives}
Returns = {rep: [] for rep in representatives}

epsilon = 0.2
episodes = 100

print("\n===== MONTE CARLO TRAINING =====")

for episode in range(episodes):

    episode_data = data.sample(frac=1)

    for _, row in episode_data.iterrows():

        # Epsilon-Greedy Policy
        if random.random() < epsilon:
            rep = random.choice(representatives)
        else:
            rep = max(Q, key=Q.get)

        handling_time = row["HandlingTime"]
        resolved = row["Resolved"]

        # Reward Function
        if resolved == 1:
            reward = 10 - handling_time
        else:
            reward = -handling_time

        Returns[rep].append(reward)
        Q[rep] = np.mean(Returns[rep])

print("\n===== STATE VALUES =====")

for rep in representatives:
    print(rep, ":", round(Q[rep], 2))

best_rep = max(Q, key=Q.get)

print("\nBest Representative Policy :", best_rep)

avg_time = data[data["Representative"] == best_rep]["HandlingTime"].mean()

print("Average Handling Time :", round(avg_time, 2), "minutes")

print("\nExperiment Completed Successfully")
