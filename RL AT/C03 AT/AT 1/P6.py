# Reward Shaping Example

position = 0
goal = 4

reward = 0

while position < goal:

    position += 1

    reward += 10

    print("Moved to position", position)

    print("Reward:", reward)

print("Goal Reached!")

reward += 100

print("Final Reward:", reward)
