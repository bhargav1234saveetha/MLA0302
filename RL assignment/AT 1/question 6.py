import random

actions = ["Left", "Right", "Up", "Down"]
values = [5, 10, 3, 8]

print("Random Strategy")
for i in range(5):
    action = random.choice(actions)
    print("Action:", action)

print("\nGreedy Strategy")
best_action = actions[values.index(max(values))]
for i in range(5):
    print("Action:", best_action)

print("\nEpsilon-Greedy Strategy")
epsilon = 0.2

for i in range(5):

    if random.random() < epsilon:
        action = random.choice(actions)
    else:
        action = best_action

    print("Action:", action)
