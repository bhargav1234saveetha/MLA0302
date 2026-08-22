import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("q25_smart_grid.csv")

# Actions
# -1 = Discharge battery
#  0 = Hold
# +1 = Charge battery

actions = np.array([-1, 0, 1])

# Initial policy probabilities
policy = np.array([0.25, 0.50, 0.25])

battery_capacity = 10
battery_start = 5

learning_rate = 0.05
max_kl = 0.02


# -----------------------------------------
# Smart Grid Environment
# -----------------------------------------

def run_episode(policy):

    battery = battery_start
    rewards = []
    chosen_actions = []

    for _, row in df.iterrows():

        # Select action
        action_index = np.random.choice(
            3,
            p=policy
        )

        action = actions[action_index]

        # Update battery
        new_battery = np.clip(
            battery + action,
            0,
            battery_capacity
        )

        actual_change = new_battery - battery

        # Renewable energy
        solar = row["Solar_kWh"]

        # Battery energy
        battery_supply = max(
            0,
            -actual_change
        )

        charging_energy = max(
            0,
            actual_change
        )

        available_energy = (
            solar
            + battery_supply
            - charging_energy
        )

        # Energy purchased from grid
        grid_energy = max(
            0,
            row["Demand_kWh"]
            - available_energy
        )

        # Electricity cost
        cost = (
            grid_energy *
            row["Grid_Price"]
        )

        # Supply-demand imbalance
        imbalance = abs(
            row["Demand_kWh"]
            - (
                solar
                + battery_supply
                + grid_energy
            )
        )

        # Reward
        reward = -(
            cost +
            10 * imbalance
        )

        battery = new_battery

        rewards.append(reward)
        chosen_actions.append(action_index)

    return np.array(rewards), chosen_actions


# -----------------------------------------
# TRPO Training
# -----------------------------------------

np.random.seed(42)

reward_history = []

for episode in range(200):

    rewards, selected = run_episode(policy)

    baseline = rewards.mean()

    new_policy = policy.copy()

    for i in range(3):

        selected_rewards = rewards[
            np.array(selected) == i
        ]

        if len(selected_rewards) > 0:

            advantage = (
                selected_rewards.mean()
                - baseline
            )

            new_policy[i] += (
                learning_rate *
                advantage / 100
            )

    # Keep probabilities positive
    new_policy = np.maximum(
        new_policy,
        0.001
    )

    # Normalize
    new_policy /= new_policy.sum()

    # Trust-region constraint
    kl = np.sum(
        policy *
        np.log(policy / new_policy)
    )

    if kl <= max_kl:
        policy = new_policy

    reward_history.append(
        rewards.sum()
    )


# -----------------------------------------
# Output
# -----------------------------------------

print("SMART GRID - TRPO")
print("------------------")

print("Final Policy:")

print("Discharge:",
      round(policy[0], 3))

print("Hold:",
      round(policy[1], 3))

print("Charge:",
      round(policy[2], 3))

print(
    "Average Reward:",
    round(np.mean(reward_history[-20:]), 2)
)

print(
    "Best Episode Reward:",
    round(max(reward_history), 2)
)
