demand = 80

if demand > 70:
    price = 120
    action = "Increase Price"
    reward = 10
elif demand < 30:
    price = 80
    action = "Decrease Price"
    reward = 5
else:
    price = 100
    action = "Keep Same Price"
    reward = 8

print("Demand:", demand)
print("Action:", action)
print("New Price:", price)
print("Reward:", reward)
