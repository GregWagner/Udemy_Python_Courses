# import modules
import gym

env = gym.make("CartPole-v1")  # version 0.15.0


num_episodes = 100  # episode from initial (game started) -> AI wins /AI loose
num_timesteps = 50


# for each episode
for i in range(num_episodes):
    # set the Return to 0
    Return = 0

    # initialize the state by resetting the environment
    state = env.reset()
    # print(state)

    # for each step in the episode
    for t in range(num_timesteps):

        # randomly select an action by sampling from the environment

        random_action = env.action_space.sample()  # AI player : agent -> Left, Right
        env.render()
        # random policy
        # perform the randomly selected action
        # tennis game: -1, 0, +1 -> reward: AI player
        next_state, reward, done, info = env.step(random_action)

        # update the return : sum of rewards
        Return = Return + reward

        # if the next state is a terminal (end) state then end the episode
        if done:
            break

    # for every 10 episodes, print the return (sum of rewards)
    if i % 10 == 0:
        print(f"Episode number: {i}, Return : {Return}")

env.close()
