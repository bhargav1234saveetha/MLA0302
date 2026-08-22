import pandas as pd
import numpy as np

# -----------------------------------------
# LOAD CSV FILE
# -----------------------------------------

df = pd.read_csv("q27_portfolio_prices.csv")

print("Portfolio Data")
print(df)
print()


# -----------------------------------------
# Stock price from CSV
# -----------------------------------------

prices = df["Stock_A"].values

# Actions
# 0 = Hold
# 1 = Buy
# 2 = Sell

actions = [0, 1, 2]


# -----------------------------------------
# Initial Actor probabilities
# -----------------------------------------

actor = np.array([
    0.33,
    0.34,
    0.33
])

critic = 0.0

actor_lr = 0.01
critic_lr = 0.01

gamma = 0.9

episodes = 200

reward_history = []


# -----------------------------------------
# Actor-Critic Training
# -----------------------------------------

for episode in range(episodes):

    money = 1000
    stocks = 0

    total_reward = 0

    for t in range(len(prices) - 1):

        # Select action
        action = np.random.choice(
            actions,
            p=actor
        )

        current_price = prices[t]

        next_price = prices[t + 1]


        # ---------------------------------
        # BUY
        # ---------------------------------

        if action == 1:

            if money >= current_price:

                stocks += 1

                money -= current_price


        # ---------------------------------
        # SELL
        # ---------------------------------

        elif action == 2:

            if stocks > 0:

                stocks -= 1

                money += current_price


        # ---------------------------------
        # Portfolio value
        # ---------------------------------

        current_value = (
            money +
            stocks * current_price
        )

        next_value = (
            money +
            stocks * next_price
        )


        # Reward
        reward = (
            next_value -
            current_value
        )


        # Risk penalty
        if reward < 0:

            reward = reward * 1.5


        # ---------------------------------
        # Critic Update
        # ---------------------------------

        td_error = (
            reward +
            gamma * critic -
            critic
        )

        critic = (
            critic +
            critic_lr * td_error
        )


        # ---------------------------------
        # Actor Update
        # ---------------------------------

        if td_error > 0:

            actor[action] += (
                actor_lr * td_error
            )

        else:

            actor[action] -= (
                actor_lr * abs(td_error)
            )


        # Keep probabilities positive
        actor = np.maximum(
            actor,
            0.01
        )


        # Normalize probabilities
        actor = (
            actor /
            np.sum(actor)
        )


        total_reward += reward


    reward_history.append(
        total_reward
    )


# -----------------------------------------
# OUTPUT
# -----------------------------------------

print("FINANCIAL PORTFOLIO MANAGEMENT")
print("Using Actor-Critic")
print("--------------------------------")

print("Final Policy Probabilities")

print(
    "Hold :",
    round(actor[0], 3)
)

print(
    "Buy  :",
    round(actor[1], 3)
)

print(
    "Sell :",
    round(actor[2], 3)
)

print()

print(
    "Average Reward:",
    round(
        np.mean(
            reward_history[-20:]
        ),
        2
    )
)

print(
    "Best Reward:",
    round(
        max(reward_history),
        2
    )
)


# -----------------------------------------
# Best Action
# -----------------------------------------

best_action = np.argmax(actor)

if best_action == 0:

    print(
        "\nLearned Policy: HOLD"
    )

elif best_action == 1:

    print(
        "\nLearned Policy: BUY"
    )

else:

    print(
        "\nLearned Policy: SELL"
    )
