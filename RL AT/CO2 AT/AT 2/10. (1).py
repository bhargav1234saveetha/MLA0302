# Smart Irrigation

soil = "Dry"
action = "Start Watering"

if soil == "Dry":
    reward = 15
else:
    reward = -5

print("State:", soil)
print("Action:", action)
print("Reward:", reward)
