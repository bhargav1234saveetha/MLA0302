import os
import pandas as pd
import random

# ==========================
# Load Dataset
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "investment_data.csv")

data = pd.read_csv(csv_file)

print("===== INVESTMENT DATA =====")
print(data)

actions = ["Buy", "Hold", "Sell"]

policy = {
    "Buy": 0.33,
    "Hold": 0.33,
    "Sell": 0.34
}

learning_rate = 0.05

print("\n===== POLICY GRADIENT TRAINING =====")

for episode in range(20):

    total_reward = 0

    for _, row in data.iterrows():

        action = random.choices(
            actions,
            weights=[policy["Buy"], policy["Hold"], policy["Sell"]]
        )[0]

        ret = row["Return"]

        if action == "Buy":
            reward = ret

        elif action == "Sell":
            reward = -ret

        else:
            reward = 0

        total_reward += reward

    if total_reward > 0:
        policy["Buy"] += learning_rate
        policy["Sell"] -= learning_rate / 2
        policy["Hold"] -= learning_rate / 2

    else:
        policy["Buy"] -= learning_rate / 2
        policy["Sell"] += learning_rate / 2
        policy["Hold"] += learning_rate / 2

    # Normalize probabilities
    total = sum(policy.values())
    for key in policy:
        policy[key] = max(policy[key], 0.01)
    total = sum(policy.values())
    for key in policy:
        policy[key] /= total

    print(f"Episode {episode+1}: Reward = {round(total_reward,2)}")

print("\n===== FINAL POLICY =====")
for action in actions:
    print(f"{action}: {policy[action]:.2f}")

best_action = max(policy, key=policy.get)

print("\nBest Investment Strategy:", best_action)
