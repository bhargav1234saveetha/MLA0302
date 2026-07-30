import gymnasium as gym

environments = ["FrozenLake-v1", "CartPole-v1", "MountainCar-v0"]

for env_name in environments:

    print("\n==============================")
    print("Environment:", env_name)
    print("==============================")

    env = gym.make(env_name)

    state, info = env.reset()

    print("Initial State:", state)

    total_reward = 0

    for i in range(5):

        action = env.action_space.sample()

        next_state, reward, terminated, truncated, info = env.step(action)

        custom_reward = reward + (i + 1)

        total_reward += custom_reward

        print("\nStep:", i + 1)
        print("Action:", action)
        print("Next State:", next_state)
        print("Reward:", custom_reward)
        print("Total Reward:", total_reward)
        print("Episode Ended:", terminated or truncated)

        if terminated or truncated:
            break

    env.close()