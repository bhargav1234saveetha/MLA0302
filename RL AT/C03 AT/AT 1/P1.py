state = "Start"

actions = ["Left", "Right"]

reward = 0

print("Current State:", state)

action = "Right"

print("Agent chooses:", action)

if action == "Right":
    reward = 10
else:
    reward = -5

print("Reward:", reward)

print("Agent learns that moving Right gives higher reward.")
