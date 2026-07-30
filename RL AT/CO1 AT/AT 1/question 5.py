gamma = 0.9

rewards = [5, 10, 15]

values = [0, 0, 0]

print("Bellman Expectation Equation")

for i in range(10):

    for j in range(3):

        values[j] = rewards[j] + gamma * values[j]

    print("Iteration", i + 1, ":", values)
