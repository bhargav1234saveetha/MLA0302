import random

agents = {
    "Agent A": 0.6,
    "Agent B": 0.8,
    "Agent C": 0.7
}

episodes = 100

values = {}

for agent in agents:

    total_reward = 0

    for i in range(episodes):

        if random.random() < agents[agent]:
            reward = 1
        else:
            reward = 0

        total_reward += reward

    values[agent] = total_reward / episodes

print("Estimated Value Function\n")

for agent, value in values.items():
    print(agent, ":", round(value, 2))
