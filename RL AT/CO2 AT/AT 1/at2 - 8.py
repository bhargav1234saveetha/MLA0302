available_bandwidth = 100
user_demand = 80

if user_demand <= available_bandwidth:
    action = "Allocate Bandwidth"
    allocated = user_demand
    reward = 10
else:
    action = "Redistribute Bandwidth"
    allocated = available_bandwidth
    reward = 5

print("Available Bandwidth:", available_bandwidth)
print("User Demand:", user_demand)
print("Action:", action)
print("Allocated:", allocated)
print("Reward:", reward)
