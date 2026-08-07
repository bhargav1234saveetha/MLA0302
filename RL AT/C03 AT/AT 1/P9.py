# Model-Free RL Example

rewards = [0, 10, -5, 20]

total_reward = 0

for reward in rewards:
    total_reward += reward
    print("Received Reward:", reward)

print("Total Reward:", total_reward)
