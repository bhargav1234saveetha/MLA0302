import pandas as pd
import numpy as np
import math

# Load CSV file
df = pd.read_csv("streaming_content_ucb_dataset.csv")

# Content names
contents = [
    "Movie_A",
    "Movie_B",
    "Series_C",
    "Sports_D",
    "Documentary_E"
]

n = len(contents)

# ---------------------------------------------------
# UCB Algorithm
# ---------------------------------------------------

counts = np.zeros(n)
rewards = np.zeros(n)

ucb_total_reward = 0

for t in range(len(df)):

    # Select every content once initially
    if t < n:
        selected = t

    else:
        ucb_values = []

        for i in range(n):

            average_reward = rewards[i] / counts[i]

            confidence = math.sqrt(
                (2 * math.log(t + 1)) / counts[i]
            )

            ucb = average_reward + confidence
            ucb_values.append(ucb)

        selected = np.argmax(ucb_values)

    # Get reward from CSV
    reward = df.iloc[t][contents[selected] + "_reward"]

    counts[selected] += 1
    rewards[selected] += reward

    ucb_total_reward += reward


# ---------------------------------------------------
# Random Strategy
# ---------------------------------------------------

np.random.seed(42)

random_total_reward = 0

for t in range(len(df)):

    selected = np.random.randint(n)

    reward = df.iloc[t][contents[selected] + "_reward"]

    random_total_reward += reward


# ---------------------------------------------------
# Epsilon-Greedy Strategy
# ---------------------------------------------------

epsilon = 0.1

counts = np.zeros(n)
rewards = np.zeros(n)

epsilon_total_reward = 0

np.random.seed(42)

for t in range(len(df)):

    # Exploration
    if np.random.random() < epsilon:
        selected = np.random.randint(n)

    # Exploitation
    else:
        if t < n:
            selected = t
        else:
            average_rewards = rewards / counts
            selected = np.argmax(average_rewards)

    reward = df.iloc[t][contents[selected] + "_reward"]

    counts[selected] += 1
    rewards[selected] += reward

    epsilon_total_reward += reward


# ---------------------------------------------------
# Popularity / Greedy Strategy
# ---------------------------------------------------

counts = np.zeros(n)
rewards = np.zeros(n)

greedy_total_reward = 0

for t in range(len(df)):

    if t < n:
        selected = t
    else:
        average_rewards = rewards / counts
        selected = np.argmax(average_rewards)

    reward = df.iloc[t][contents[selected] + "_reward"]

    counts[selected] += 1
    rewards[selected] += reward

    greedy_total_reward += reward


# ---------------------------------------------------
# Compare Results
# ---------------------------------------------------

results = pd.DataFrame({
    "Strategy": [
        "UCB",
        "Random",
        "Epsilon-Greedy",
        "Popularity/Greedy"
    ],

    "Total Reward": [
        ucb_total_reward,
        random_total_reward,
        epsilon_total_reward,
        greedy_total_reward
    ]
})

# Calculate engagement percentage
results["Engagement (%)"] = (
    results["Total Reward"] / len(df) * 100
)

print("\nPerformance Comparison")
print("----------------------")
print(results.to_string(index=False))

# Find best strategy
best = results.loc[
    results["Total Reward"].idxmax()
]

print("\nBest Strategy:")
print(best["Strategy"])

print("\nUCB Total Reward:", ucb_total_reward)
print("UCB Engagement:", round(ucb_total_reward / len(df) * 100, 2), "%")
