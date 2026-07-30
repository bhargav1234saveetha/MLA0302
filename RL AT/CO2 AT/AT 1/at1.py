import random

routes = ["Route A", "Route B", "Route C"]
rewards = [5, 10, 3]

for i in range(5):
    route = random.randint(0, 2)
    print("Selected:", routes[route])
    print("Reward:", rewards[route])

best = rewards.index(max(rewards))

print("Best Route:", routes[best])
