# Healthcare RL

patient = "Stable"
action = "Maintain Dose"

improved = True

if improved:
    reward = 20
else:
    reward = -15

print("Patient:", patient)
print("Action:", action)
print("Reward:", reward)
