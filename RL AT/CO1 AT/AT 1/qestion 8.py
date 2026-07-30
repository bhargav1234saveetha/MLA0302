import random
import matplotlib.pyplot as plt

episodes = 10

episode_rewards = []
cumulative_rewards = []

total_reward = 0

for episode in range(episodes):

    reward = random.randint(1, 10)

    episode_rewards.append(reward)

    total_reward += reward

    cumulative_rewards.append(total_reward)

print("Episode Rewards:", episode_rewards)
print("Cumulative Rewards:", cumulative_rewards)

plt.figure(figsize=(8,5))

plt.plot(range(1, episodes + 1), episode_rewards,
         marker='o', label="Episode Reward")

plt.plot(range(1, episodes + 1), cumulative_rewards,
         marker='s', label="Cumulative Reward")

plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Reward Visualization in Reinforcement Learning")
plt.legend()

plt.grid(True)

plt.show()
