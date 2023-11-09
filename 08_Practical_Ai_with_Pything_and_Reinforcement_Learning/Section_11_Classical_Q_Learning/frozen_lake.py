# ToDo - plotting is not working

import time
import gym
import numpy as np
import matplotlib.pyplot as plt

from gym.envs.registration import register


# Register a custom environment without slipping
try:
    register(
        id="FrozenLakeNotSlippery-v0",  # make sure this is a custom name!
        entry_point="gym.envs.toy_text:FrozenLakeEnv",
        kwargs={"map_name": "4x4", "is_slippery": False},
        max_episode_steps=100,
        reward_threshold=0.8196,
    )
except:
    print("You probably ran this cell twice, accidentally trying to register")
    print("a new env with the same id twice.")
    print("Either change the id, or just continue, knowing your id was")
    print("already registered")

env = gym.make("FrozenLakeNotSlippery-v0")

# Create the initial Q-Table
action_size = env.action_space.n
state_size = env.observation_space.n
q_table = np.zeros([state_size, action_size])
print(f"Q Table is {state_size} x {action_size}")


# Hyperparameters
EPOCHS = 10000  # how many times to play the game
ALPHA = 0.8  # learning rate
GAMMA = 0.95  # discount rate
epsilon = 1.0  # exploration rate
max_epsilon = 1.0  # exploration probability at start
min_epsilon = 0.01  # minimum exploration probability
decay_rate = 0.001  # exponential decay rate for exploration probability


def random_action():
    return env.action_space.sample()


def epsilon_greedy_action_selection(epsilon, q_table, discrete_state):
    random_number = np.random.random()

    if random_number > epsilon:
        # Exploitation (choose the action that maximized Q)
        state_row = q_table[discrete_state, :]
        action = np.argmax(state_row)
    else:
        # Exploration (choose a random action)
        action = random_action()

    return action


def compute_next_q_value(old_q_value, reward, next_optimal_q_value):
    return old_q_value + ALPHA * (reward + GAMMA * next_optimal_q_value - old_q_value)


def reduce_epsilon(epsilon, epoch):
    return min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * epoch)


rewards = []

#####################################
# Visualzation of training progress
#####################################
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.canvas.draw()
log_interval = 1000
epoch_plot_tracker = []
total_reward_plot_tracker = []
#####################################

for episode in range(EPOCHS):
    state = env.reset()
    # env.render()

    done = False
    total_rewards = 0
    while not done:
        # Select and perform action
        action = epsilon_greedy_action_selection(epsilon, q_table, state)
        new_state, reward, done, info = env.step(action)

        # Get Old (current) Q value (i.e Q(s, a))
        old_q_value = q_table[state, action]

        # Get next optimal Q value (max Q value for this state) (i.e. Q(st+1, at+1))
        next_optimal_q_value = np.max(q_table[new_state, :])

        # Compute the next Q value
        next_q = compute_next_q_value(old_q_value, reward, next_optimal_q_value)

        # update the table
        q_table[state, action] = next_q

        # track rewards
        total_rewards += reward

        # new state is now state
        state = new_state

    # agent finished a round of the game
    episode += 1
    epsilon = reduce_epsilon(epsilon, episode)
    rewards.append(total_rewards)

    total_reward_plot_tracker.append(np.sum(rewards))
    epoch_plot_tracker.append(episode)
    # Plot the points and running mean
    if episode % log_interval == 0:
        print(np.sum(rewards))
        ax.clear()
        ax.plot(epoch_plot_tracker, total_reward_plot_tracker)
        fig.canvas.draw()
#####################################

# q-table is filled in - now play the game
state = env.reset()
for _ in range(100):
    env.render()
    action = np.argmax(q_table[state, :])
    state, reward, done, info = env.step(action)

    time.sleep(1)

    if done:
        break

print(q_table)
env.close()
