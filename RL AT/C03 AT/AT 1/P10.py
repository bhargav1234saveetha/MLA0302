# Simple Q-Learning Update

Q = 5          # Current Q-value
alpha = 0.5    # Learning rate
gamma = 0.9    # Discount factor

reward = 10

future_q = 8

new_Q = Q + alpha * (reward + gamma * future_q - Q)

print("Old Q-value:", Q)
print("Updated Q-value:", new_Q)
