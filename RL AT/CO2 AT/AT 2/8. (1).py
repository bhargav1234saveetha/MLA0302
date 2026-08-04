# Manufacturing Robot

completed = 15
errors = 2

value = completed - errors

if value > 10:
    policy = "Continue Current Process"
else:
    policy = "Improve Strategy"

print("Policy:", policy)
print("Value Function:", value)
