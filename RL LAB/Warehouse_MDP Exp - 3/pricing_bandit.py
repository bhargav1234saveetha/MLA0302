import os
import pandas as pd
import numpy as np
import random
import math

# ==========================
# Load CSV
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "pricing_data.csv")

data = pd.read_csv(csv_file)

print("===== PRICING DATASET =====")
print(data)

prices = data["Price"].tolist()
rewards = data["Revenue"].tolist()

n_arms = len(prices)
rounds = 100

# ==========================
# EPSILON GREEDY
# ==========================

epsilon = 0.1
counts = [0] * n_arms
values = [0] * n_arms
total_reward_eps = 0

for t in range(rounds):

    if random.random() < epsilon:
        arm = random.randint(0, n_arms - 1)
    else:
        arm = np.argmax(values)

    reward = rewards[arm]

    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

    total_reward_eps += reward

print("\nEpsilon-Greedy Revenue =", total_reward_eps)

# ==========================
# UCB
# ==========================

counts = [0] * n_arms
values = [0] * n_arms
total_reward_ucb = 0

for t in range(rounds):

    if t < n_arms:
        arm = t
    else:
        ucb = []

        for i in range(n_arms):
            bonus = math.sqrt((2 * math.log(t + 1)) / counts[i])
            ucb.append(values[i] + bonus)

        arm = np.argmax(ucb)

    reward = rewards[arm]

    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

    total_reward_ucb += reward

print("UCB Revenue =", total_reward_ucb)

# ==========================
# THOMPSON SAMPLING
# ==========================

success = [1] * n_arms
failure = [1] * n_arms

total_reward_ts = 0

for t in range(rounds):

    samples = []

    for i in range(n_arms):
        samples.append(np.random.beta(success[i], failure[i]))

    arm = np.argmax(samples)

    reward = rewards[arm]

    total_reward_ts += reward

    if reward >= np.mean(rewards):
        success[arm] += 1
    else:
        failure[arm] += 1

print("Thompson Sampling Revenue =", total_reward_ts)

# ==========================
# Best Strategy
# ==========================

print("\n===== FINAL RESULT =====")

print("Epsilon-Greedy :", total_reward_eps)
print("UCB            :", total_reward_ucb)
print("Thompson       :", total_reward_ts)

best = max(total_reward_eps, total_reward_ucb, total_reward_ts)

if best == total_reward_eps:
    print("\nBest Strategy : Epsilon-Greedy")

elif best == total_reward_ucb:
    print("\nBest Strategy : UCB")

else:
    print("\nBest Strategy : Thompson Sampling")
