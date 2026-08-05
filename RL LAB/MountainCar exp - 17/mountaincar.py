import gymnasium as gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import random

env = gym.make("MountainCar-v0")

state_size = env.observation_space.shape[0]
action_size = env.action_space.n

model = Sequential([
    Dense(24, input_dim=state_size, activation='relu'),
    Dense(24, activation='relu'),
    Dense(action_size, activation='linear')
])

model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))

episodes = 10

print("===== TRAINING =====")

for episode in range(episodes):

    state, _ = env.reset()
    state = np.reshape(state, [1, state_size])

    total_reward = 0

    for step in range(200):

        if random.random() < 0.2:
            action = env.action_space.sample()
        else:
            q = model.predict(state, verbose=0)
            action = np.argmax(q[0])

        next_state, reward, terminated, truncated, _ = env.step(action)

        done = terminated or truncated

        next_state = np.reshape(next_state, [1, state_size])

        target = reward

        if not done:
            target = reward + 0.95 * np.max(model.predict(next_state, verbose=0)[0])

        target_f = model.predict(state, verbose=0)
        target_f[0][action] = target

        model.fit(state, target_f, epochs=1, verbose=0)

        state = next_state
        total_reward += reward

        if done:
            break

    print("Episode", episode + 1, "Reward =", total_reward)

print("\nTraining Completed Successfully")

env.close()
