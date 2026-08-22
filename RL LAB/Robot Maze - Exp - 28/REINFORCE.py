import pandas as pd
import numpy as np

# -----------------------------------------
# LOAD MAZE FROM CSV
# -----------------------------------------

df = pd.read_csv("q28_maze.csv")

maze = df.values.tolist()

print("Maze Loaded From CSV")
print("---------------------")

for row in maze:
    print(row)

print()


# -----------------------------------------
# Maze dimensions
# -----------------------------------------

rows = len(maze)
cols = len(maze[0])


# -----------------------------------------
# Find Start and Goal
# -----------------------------------------

for r in range(rows):

    for c in range(cols):

        if maze[r][c] == "S":

            start = (r, c)

        if maze[r][c] == "G":

            goal = (r, c)


# -----------------------------------------
# Actions
# -----------------------------------------

# 0 = Up
# 1 = Down
# 2 = Left
# 3 = Right

actions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

symbols = [
    "↑",
    "↓",
    "←",
    "→"
]


# -----------------------------------------
# Policy
# -----------------------------------------

policy = np.ones(
    (rows, cols, 4)
) / 4


learning_rate = 0.1

gamma = 0.9

episodes = 1000


# -----------------------------------------
# Move Function
# -----------------------------------------

def move(state, action):

    r, c = state

    dr, dc = actions[action]

    new_r = r + dr

    new_c = c + dc


    # Outside maze
    if (
        new_r < 0 or
        new_r >= rows or
        new_c < 0 or
        new_c >= cols
    ):

        return state, -2


    # Wall
    if maze[new_r][new_c] == "X":

        return state, -2


    # Goal
    if (
        new_r,
        new_c
    ) == goal:

        return (
            new_r,
            new_c
        ), 10


    # Normal movement
    return (
        new_r,
        new_c
    ), -0.1


# -----------------------------------------
# REINFORCE TRAINING
# -----------------------------------------

reward_history = []


for episode in range(episodes):

    state = start

    states = []

    selected_actions = []

    rewards = []


    # Maximum 100 steps
    for step in range(100):

        r, c = state


        # Select action using policy
        action = np.random.choice(
            4,
            p=policy[r, c]
        )


        # Move robot
        next_state, reward = move(
            state,
            action
        )


        states.append(state)

        selected_actions.append(
            action
        )

        rewards.append(
            reward
        )


        state = next_state


        # Stop when goal reached
        if state == goal:

            break


    # -------------------------------------
    # Calculate Returns
    # -------------------------------------

    returns = []

    G = 0


    for reward in reversed(rewards):

        G = (
            reward +
            gamma * G
        )

        returns.insert(
            0,
            G
        )


    # -------------------------------------
    # Update Policy
    # -------------------------------------

    for i in range(
        len(states)
    ):

        r, c = states[i]

        action = selected_actions[i]

        G = returns[i]


        # Increase/decrease probability
        policy[
            r,
            c,
            action
        ] += (
            learning_rate * G
        )


        # Keep probabilities positive
        policy[
            r,
            c
        ] = np.maximum(
            policy[
                r,
                c
            ],
            0.001
        )


        # Normalize
        policy[
            r,
            c
        ] /= np.sum(
            policy[
                r,
                c
            ]
        )


    reward_history.append(
        sum(rewards)
    )


# -----------------------------------------
# OUTPUT
# -----------------------------------------

print("ROBOT MAZE NAVIGATION")
print("Using REINFORCE")
print("---------------------")

print(
    "Average Reward:",
    round(
        np.mean(
            reward_history[-50:]
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
# Display Learned Policy
# -----------------------------------------

print("\nLearned Maze Policy")
print("-------------------")


for r in range(rows):

    row = ""

    for c in range(cols):

        if maze[r][c] == "X":

            row += " X "

        elif maze[r][c] == "G":

            row += " G "

        else:

            best_action = np.argmax(
                policy[r, c]
            )

            row += (
                " "
                + symbols[best_action]
                + " "
            )

    print(row)
