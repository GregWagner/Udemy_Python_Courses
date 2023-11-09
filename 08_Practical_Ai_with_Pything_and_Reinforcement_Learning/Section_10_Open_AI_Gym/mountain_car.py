import gym
import time


def simple_agent(observation):
    # Observation
    position, velocity = observation

    if -0.1 < position < 0.4:
        action = 2
    elif velocity < 0 and position < -0.2:
        action = 0
    else:
        action = 1

    # Action
    return action


env_name = "MountainCar-v0"
env = gym.make(env_name)

observation = env.reset(seed=42)

# show how many actions are available
print(f"Number of actions: {env.action_space.n}")

for _ in range(200):
    env.render(mode="human")
    # cart goes right
    action = simple_agent(observation)
    observation, reward, done, info = env.step(action)

    print(f"Position: {observation[0]}")
    print(f"Velociity: {observation[1]}")

    if done:
        break

    time.sleep(0.1)

env.close()
