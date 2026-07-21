import random
import math

rewards = [5, 10, 7]

print("Epsilon-Greedy")

epsilon = 0.2
total_reward = 0

for i in range(10):

    if random.random() < epsilon:
        action = random.randint(0, 2)
    else:
        action = rewards.index(max(rewards))

    reward = rewards[action]
    total_reward += reward

    print("Step:", i+1, "Action:", action, "Reward:", reward)

print("Total Reward:", total_reward)


print("\nUpper Confidence Bound (UCB)")

counts = [1, 1, 1]
values = rewards.copy()
total_reward = 0

for i in range(10):

    ucb = []

    for j in range(3):
        value = values[j] + math.sqrt((2 * math.log(i + 4)) / counts[j])
        ucb.append(value)

    action = ucb.index(max(ucb))

    reward = rewards[action]
    total_reward += reward
    counts[action] += 1

    print("Step:", i+1, "Action:", action, "Reward:", reward)

print("Total Reward:", total_reward)
