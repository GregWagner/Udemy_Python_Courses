import gym

env = gym.make('ALE/Breakout-v5',
    obs_type='rgb',                   # ram | rgb | grayscale
    frameskip=4,                      # frame skip
    mode=None,                        # game mode, see Machado et al. 2018
    difficulty=None,                  # game difficulty, see Machado et al. 2018
    repeat_action_probability=0.25,   # Sticky action probability
    full_action_space=False,          # Use all actions
    render_mode='human'                  # None | human | rgb_array
)

env.reset(seed=42, return_info=True)

for _ in range(2000):
    random_action = env.action_space.sample()
    observation, reward, done, info = env.step(random_action)

    print(f"Reward: {reward}")
    print(f"Done: {done}")
    print(f"Info: {info}")


env.close()
