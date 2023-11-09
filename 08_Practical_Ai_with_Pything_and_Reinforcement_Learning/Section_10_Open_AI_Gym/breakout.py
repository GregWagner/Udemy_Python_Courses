import gym
import time

env = gym.make(
    "ALE/Breakout-v5",
    obs_type="rgb",  # ram | rgb | grayscale
    frameskip=4,  # frame skip
    mode=None,  # game mode
    difficulty=None,  # game difficulty
    repeat_action_probability=0.25,  # Sticky action probability
    full_action_space=False,  # Use all actions
    render_mode="human",  # None | human | rgb_array
)

env.reset(seed=42, return_info=True)

# show how many actions are available
print(f"Number of actions: {env.action_space.n}")

for _ in range(200):
    # get a possible random action
    random_action = env.action_space.sample()
    observation, reward, done, info = env.step(random_action)

    print(f"Taking action: {random_action}")
    print(f"Reward: {reward}")
    print(f"Done: {done}")
    print(f"Info: {info}")

    if done:
        break

    time.sleep(0.05)

env.close()
