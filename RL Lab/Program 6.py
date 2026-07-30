import random
import math

ads = [0.2, 0.5, 0.8]
steps = 100

def click(ad):
    return 1 if random.random() < ads[ad] else 0

def epsilon_greedy():
    epsilon = 0.1
    count = [0, 0, 0]
    value = [0, 0, 0]
    total = 0

    for i in range(steps):

        if random.random() < epsilon:
            ad = random.randint(0, 2)
        else:
            ad = value.index(max(value))

        r = click(ad)
        count[ad] += 1
        value[ad] += (r - value[ad]) / count[ad]
        total += r

    return total

def ucb():
    count = [1, 1, 1]
    value = [0, 0, 0]
    total = 0

    for i in range(3):
        r = click(i)
        value[i] = r
        total += r

    for t in range(3, steps):

        ucb_value = []

        for i in range(3):
            x = value[i] + math.sqrt((2 * math.log(t + 1)) / count[i])
            ucb_value.append(x)

        ad = ucb_value.index(max(ucb_value))

        r = click(ad)
        count[ad] += 1
        value[ad] += (r - value[ad]) / count[ad]
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

        ad = sample.index(max(sample))

        r = click(ad)

        if r == 1:
            success[ad] += 1
        else:
            failure[ad] += 1

        total += r

    return total

eg = epsilon_greedy()
ucb_result = ucb()
ts = thompson()

print("Epsilon Greedy Clicks :", eg)
print("UCB Clicks :", ucb_result)
print("Thompson Sampling Clicks :", ts)

best = max(eg, ucb_result, ts)

if best == eg:
    print("Best Algorithm : Epsilon Greedy")
elif best == ucb_result:
    print("Best Algorithm : UCB")
else:
    print("Best Algorithm : Thompson Sampling")
