import random

for i in range(5):

    transaction = random.randint(100, 100000)

    if transaction > 50000:
        action = "Review"
        reward = 10
    else:
        action = "Approve"
        reward = 5

    print("Amount:", transaction)
    print("Action:", action)
    print("Reward:", reward)
