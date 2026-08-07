import random

attempts = 0

success = False

while not success:

    attempts += 1

    action = random.choice(["Correct", "Wrong"])

    if action == "Correct":
        success = True
        print("Task Completed!")

    else:
        print("Failed Attempt")

print("Total Attempts:", attempts)
