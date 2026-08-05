import os
import pandas as pd
import numpy as np
import random

# ==========================
# Read Dataset
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "content_recommendation.csv")

data = pd.read_csv(csv_file)

print("===== CONTENT DATA =====")
print(data)

contents = data["ContentID"].tolist()
ctr = data["CTR"].tolist()

n = len(contents)

epsilon = 0.1
runs = 1000

counts = [0]*n
values = [0]*n

total_reward = 0

print("\n===== EPSILON GREEDY TRAINING =====")

for run in range(runs):

    # Exploration
    if random.random() < epsilon:
        action = random.randint(0,n-1)

    # Exploitation
    else:
        action = np.argmax(values)

    reward = 1 if random.random() < ctr[action] else 0

    counts[action] += 1

    values[action] += (reward-values[action])/counts[action]

    total_reward += reward

print("\n===== RESULTS =====")

print("Total Clicks :", total_reward)

print("Average CTR :", round(total_reward/runs,3))

best = np.argmax(values)

print("\nBest Recommended Content")

print("Content ID :", contents[best])

print("Category :", data['Category'][best])

print("Estimated CTR :", round(values[best],3))

print("\n===== VALUE FUNCTION =====")

for i in range(n):

    print(contents[i],"=",round(values[i],3))

print("\nExperiment Completed Successfully")
