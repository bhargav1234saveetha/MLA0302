import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("inventory_demand_bellman.csv")

# Bellman model parameters
max_inventory = 6
max_order = 4

holding_cost = 2
order_cost = 3
shortage_cost = 8

gamma = 0.9

# Find demand probabilities from CSV
demand_values = sorted(df["Demand"].unique())

demand_prob = {
    d: (df["Demand"] == d).mean()
    for d in demand_values
}

# Initial value function
V = np.zeros(max_inventory + 1)

# Optimal policy
policy = np.zeros(max_inventory + 1, dtype=int)


# -------------------------------
# Bellman Value Iteration
# -------------------------------

for iteration in range(500):

    new_V = np.zeros(max_inventory + 1)

    for inventory in range(max_inventory + 1):

        best_cost = float("inf")
        best_order = 0

        # Try different order quantities
        for order in range(max_order + 1):

            total_cost = order_cost * order

            for demand in demand_values:

                probability = demand_prob[demand]

                remaining = inventory + order - demand

                # Holding cost
                if remaining >= 0:

                    current_cost = holding_cost * remaining

                    next_state = min(
                        remaining,
                        max_inventory
                    )

                # Shortage cost
                else:

                    current_cost = (
                        shortage_cost *
                        (-remaining)
                    )

                    next_state = 0

                # Bellman's equation
                total_cost += probability * (
                    current_cost +
                    gamma * V[next_state]
                )

            # Select minimum-cost action
            if total_cost < best_cost:

                best_cost = total_cost
                best_order = order

        new_V[inventory] = best_cost
        policy[inventory] = best_order

    # Check convergence
    if np.max(np.abs(new_V - V)) < 0.000001:

        V = new_V
        break

    V = new_V


# -------------------------------
# Display Optimal Policy
# -------------------------------

result = pd.DataFrame({

    "Inventory_Level":
        range(max_inventory + 1),

    "Optimal_Order":
        policy,

    "Minimum_Cost":
        np.round(V, 2)
})


print("INVENTORY MANAGEMENT USING BELLMAN'S EQUATION")
print("-----------------------------------------------")

print(result.to_string(index=False))


print("\nDemand data from CSV:")
print(df.to_string(index=False))


print("\nOptimal order when inventory is 0:",
      policy[0])

print("Minimum expected cost at inventory 0:",
      round(V[0], 2))
