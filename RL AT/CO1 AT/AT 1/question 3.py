import random

states = ["A", "B", "C", "Goal"]
actions = ["Left", "Right"]

state = "A"

print("Initial State:", state)

while state != "Goal":

    action = random.choice(actions)

    print("\nCurrent State:", state)
    print("Action:", action)

    if state == "A":
        state = "B"

    elif state == "B":
        state = "C"

    elif state == "C":
        state = "Goal"

    reward = 10 if state == "Goal" else -1

    print("Next State:", state)
    print("Reward:", reward)

print("\nGoal Reached!")
print("Episode Finished")
