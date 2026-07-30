solar_energy = 80
energy_demand = 50

if solar_energy > energy_demand:
    extra_energy = solar_energy - energy_demand
    action = "Store Energy"
    reward = 10

elif solar_energy < energy_demand:
    extra_energy = energy_demand - solar_energy
    action = "Use Battery Energy"
    reward = 5

else:
    extra_energy = 0
    action = "Use Solar Energy"
    reward = 8

print("Solar Energy:", solar_energy)
print("Energy Demand:", energy_demand)
print("Action:", action)
print("Energy Difference:", extra_energy)
print("Reward:", reward)
