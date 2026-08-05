import os
import pandas as pd
import numpy as np
import random
import math

# Load Dataset
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "advertisement_data.csv")

data = pd.read_csv(csv_file)

print("===== Advertisement Dataset =====")
print(data)

ads = data["Advertisement"].tolist()
ctr = data["CTR"].tolist()

n_ads = len(ads)
rounds = 1000

# -----------------------------
# Epsilon Greedy
# -----------------------------
epsilon = 0.1
counts = [0] * n_ads
values = [0] * n_ads
clicks_eps = 0

for t in range(rounds):

    if random.random() < epsilon:
        ad = random.randint(0, n_ads - 1)
    else:
        ad = np.argmax(values)

    reward = 1 if random.random() < ctr[ad] else 0

    counts[ad] += 1
    values[ad] += (reward - values[ad]) / counts[ad]
    clicks_eps += reward

# -----------------------------
# UCB
# -----------------------------
counts = [0] * n_ads
values = [0] * n_ads
clicks_ucb = 0

for t in range(rounds):

    if t < n_ads:
        ad = t
    else:
        ucb = []
        for i in range(n_ads):
            bonus = math.sqrt((2 * math.log(t + 1)) / counts[i])
            ucb.append(values[i] + bonus)
        ad = np.argmax(ucb)

    reward = 1 if random.random() < ctr[ad] else 0

    counts[ad] += 1
    values[ad] += (reward - values[ad]) / counts[ad]
    clicks_ucb += reward

# -----------------------------
# Thompson Sampling
# -----------------------------
success = [1] * n_ads
failure = [1] * n_ads
clicks_ts = 0

for t in range(rounds):

    samples = [np.random.beta(success[i], failure[i]) for i in range(n_ads)]

    ad = np.argmax(samples)

    reward = 1 if random.random() < ctr[ad] else 0

    if reward == 1:
        success[ad] += 1
    else:
        failure[ad] += 1

    clicks_ts += reward

# -----------------------------
# Results
# -----------------------------
print("\n========== RESULTS ==========")

print("Epsilon Greedy Clicks :", clicks_eps)
print("UCB Clicks            :", clicks_ucb)
print("Thompson Clicks       :", clicks_ts)

best = max(clicks_eps, clicks_ucb, clicks_ts)

if best == clicks_eps:
    print("\nBest Algorithm : Epsilon Greedy")
elif best == clicks_ucb:
    print("\nBest Algorithm : UCB")
else:
    print("\nBest Algorithm : Thompson Sampling")
