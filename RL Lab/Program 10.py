import random

prob = 0.5
learning_rate = 0.05
episodes = 100

total_reward = 0

for i in range(episodes):

    if random.random() < prob:
        action = "Invest"
        reward = random.randint(-5, 10)
    else:
        action = "Hold"
        reward = 0

    total_reward += reward

    if reward > 0:
        prob = min(1, prob + learning_rate)
    else:
        prob = max(0, prob - learning_rate)

print("Final Investment Probability :", round(prob, 2))
print("Total Reward :", total_reward)
