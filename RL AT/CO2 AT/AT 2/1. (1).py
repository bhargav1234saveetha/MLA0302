# Ride-Sharing RL Simulation

state = "Passenger Waiting"
action = "Assign Nearest Driver"

waiting_time = 3

if waiting_time <= 5:
    reward = 10
else:
    reward = -5

print("State:", state)
print("Action:", action)
print("Reward:", reward)
