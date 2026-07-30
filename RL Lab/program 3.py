import random
import math

prices = [100, 200, 300]
prob = [0.3, 0.5, 0.7]
steps = 100

def reward(arm):
    if random.random() < prob[arm]:
        return prices[arm]
    return 0

def epsilon_greedy():
    eps = 0.1
    count = [0, 0, 0]
    value = [0, 0, 0]
    total = 0

    for i in range(steps):

        if random.random() < eps:
            arm = random.randint(0, 2)
        else:
            arm = value.index(max(value))

        r = reward(arm)
        count[arm] += 1
        value[arm] += (r - value[arm]) / count[arm]
        total += r

    return total

def ucb():
    count = [1, 1, 1]
    value = [0, 0, 0]
    total = 0

    for i in range(3):
        r = reward(i)
        value[i] = r
        total += r

    for t in range(3, steps):

        ucb_value = []

        for i in range(3):
            x = value[i] + math.sqrt((2 * math.log(t + 1)) / count[i])
            ucb_value.append(x)

        arm = ucb_value.index(max(ucb_value))

        r = reward(arm)
        count[arm] += 1
        value[arm] += (r - value[arm]) / count[arm]
        total += r

    return total

def thompson():
    success = [1, 1, 1]
    failure = [1, 1, 1]
    total = 0

    for i in range(steps):

        sample = []

        for j in range(3):
            sample.append(random.betavariate(success[j], failure[j]))

        arm = sample.index(max(sample))

        r = reward(arm)

        if r > 0:
            success[arm] += 1
        else:
            failure[arm] += 1

        total += r

    return total

eg = epsilon_greedy()
ucb = ucb()
ts = thompson()

print("Epsilon Greedy Revenue :", eg)
print("UCB Revenue :", ucb)
print("Thompson Sampling Revenue :", ts)
