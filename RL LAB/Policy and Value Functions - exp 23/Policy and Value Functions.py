import numpy as np
import matplotlib.pyplot as plt

# Grid size
rows = 4
cols = 4

# Goal position
goal = (3, 3)

# Obstacle
obstacle = (1, 1)

# Actions
actions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Discount factor
gamma = 0.9


# --------------------------------------------------
# Function to calculate next state
# --------------------------------------------------

def next_state(state, action):

    r, c = state

    dr, dc = actions[action]

    new_r = r + dr
    new_c = c + dc

    # Check boundaries
    if new_r < 0 or new_r >= rows:
        return state

    if new_c < 0 or new_c >= cols:
        return state

    # Check obstacle
    if (new_r, new_c) == obstacle:
        return state

    return (new_r, new_c)


# --------------------------------------------------
# Random Policy
# --------------------------------------------------

def random_policy(state):

    return np.random.choice(list(actions.keys()))


# --------------------------------------------------
# Goal-Directed Policy
# --------------------------------------------------

def goal_policy(state):

    r, c = state

    if r < goal[0]:
        return "down"

    elif c < goal[1]:
        return "right"

    elif r > goal[0]:
        return "up"

    else:
        return "left"


# --------------------------------------------------
# Calculate Value Function
# --------------------------------------------------

def calculate_value(policy, episodes=500):

    values = np.zeros((rows, cols))

    visit_count = np.zeros((rows, cols))

    for episode in range(episodes):

        state = (0, 0)

        for step in range(30):

            if state == goal:
                break

            action = policy(state)

            new_state = next_state(state, action)

            # Reward
            if new_state == goal:
                reward = 10
            elif new_state == state:
                reward = -1
            else:
                reward = -0.1

            values[state] += reward * (gamma ** step)

            visit_count[state] += 1

            state = new_state

    # Average values
    for r in range(rows):
        for c in range(cols):

            if visit_count[r, c] > 0:
                values[r, c] /= visit_count[r, c]

    return values


# --------------------------------------------------
# Calculate values for both policies
# --------------------------------------------------

random_values = calculate_value(random_policy)

goal_values = calculate_value(goal_policy)


# --------------------------------------------------
# Print results
# --------------------------------------------------

print("Value Function - Random Policy")
print(random_values)

print("\nValue Function - Goal-Directed Policy")
print(goal_values)


# --------------------------------------------------
# Visualize Random Policy
# --------------------------------------------------

plt.figure(figsize=(6, 5))

plt.imshow(random_values)

plt.colorbar(label="Value")

plt.title("Value Function - Random Policy")

for r in range(rows):
    for c in range(cols):

        if (r, c) == obstacle:
            text = "X"

        elif (r, c) == goal:
            text = "G"

        else:
            text = round(random_values[r, c], 2)

        plt.text(c, r, text,
                 ha="center",
                 va="center")

plt.xlabel("Column")
plt.ylabel("Row")

plt.show()


# --------------------------------------------------
# Visualize Goal-Directed Policy
# --------------------------------------------------

plt.figure(figsize=(6, 5))

plt.imshow(goal_values)

plt.colorbar(label="Value")

plt.title("Value Function - Goal-Directed Policy")

for r in range(rows):
    for c in range(cols):

        if (r, c) == obstacle:
            text = "X"

        elif (r, c) == goal:
            text = "G"

        else:
            text = round(goal_values[r, c], 2)

        plt.text(c, r, text,
                 ha="center",
                 va="center")

plt.xlabel("Column")
plt.ylabel("Row")

plt.show()
