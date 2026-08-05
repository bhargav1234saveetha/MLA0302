import os
import pandas as pd
import numpy as np
import random

# ==========================
# Load Dataset
# ==========================
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "stock_trading_data.csv")

data = pd.read_csv(csv_file)

print("===== STOCK DATA =====")
print(data.head())

prices = data["Close"].values

# Actions
actions = ["BUY", "SELL", "HOLD"]

# Q Tables (Double DQN Concept)
Q1 = np.zeros((len(prices), 3))
Q2 = np.zeros((len(prices), 3))

alpha = 0.1
gamma = 0.9
epsilon = 0.2

episodes = 50

best_profit = 0

print("\n===== TRAINING =====")

for episode in range(episodes):

    balance = 1000
    shares = 0

    for state in range(len(prices)-1):

        # Epsilon-Greedy Action
        if random.random() < epsilon:
            action = random.randint(0,2)
        else:
            action = np.argmax(Q1[state] + Q2[state])

        price = prices[state]

        reward = 0

        # BUY
        if action == 0:

            if balance >= price:
                balance -= price
                shares += 1

        # SELL
        elif action == 1:

            if shares > 0:
                balance += price
                shares -= 1
                reward = price - prices[state-1]

        # HOLD
        else:
            reward = 0

        next_state = state + 1

        # Double DQN Update
        if random.random() < 0.5:

            best_action = np.argmax(Q1[next_state])

            Q1[state,action] += alpha * (
                reward +
                gamma * Q2[next_state,best_action]
                - Q1[state,action]
            )

        else:

            best_action = np.argmax(Q2[next_state])

            Q2[state,action] += alpha * (
                reward +
                gamma * Q1[next_state,best_action]
                - Q2[state,action]
            )

    final_balance = balance + shares * prices[-1]
    profit = final_balance - 1000

    if profit > best_profit:
        best_profit = profit

    print("Episode",episode+1,"Profit =",round(profit,2))

print("\n===== RESULT =====")
print("Maximum Profit =",round(best_profit,2))

print("\nLearned Policy")

for i in range(len(prices)):

    best = np.argmax(Q1[i] + Q2[i])

    print(
        "Day",
        i+1,
        "Price =",
        prices[i],
        "Action =",
        actions[best]
    )
