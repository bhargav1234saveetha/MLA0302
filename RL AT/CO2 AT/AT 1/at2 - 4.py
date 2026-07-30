temperature = 95
vibration = 80

if temperature > 90 and vibration > 70:
    action = "Perform Maintenance"
    reward = 10
else:
    action = "Continue Operation"
    reward = 5

print("Temperature:", temperature)
print("Vibration:", vibration)
print("Action:", action)
print("Reward:", reward)
