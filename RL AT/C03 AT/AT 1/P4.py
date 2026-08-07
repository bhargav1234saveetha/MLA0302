# Policy and Value Function Example

state = "Home"

policy = "Study"

reward = 10

future_reward = 20

gamma = 0.9

value = reward + gamma * future_reward

print("Current State:", state)
print("Policy:", policy)
print("Reward:", reward)
print("Future Reward:", future_reward)
print("Total Value:", value)
