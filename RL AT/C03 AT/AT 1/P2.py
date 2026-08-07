state = "Start"

actions = ["Left", "Right"]

print("Current State:", state)


action = "Right"

print("Chosen Action:", action)


if action == "Right":
    reward = 10
else:
    reward = -5

print("Reward Received:", reward)


cumulative_reward = reward

print("Cumulative Reward:", cumulative_reward)
