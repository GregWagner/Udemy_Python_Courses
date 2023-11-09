import time

import gym
import matplotlib.pyplot as plt
from gym.utils import play

env_name = "Breakout-v4"
env = gym.make(env_name)

play.play(env, zoom = 3,
        keys_to_action={"NOOP" : 0, "FIRE" : 1, "RIGHT" : 2, "LEFT" :3})
