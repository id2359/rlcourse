import gym
import lib
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


GAMMA = 1.0
ALPHA = 0.5
EPSILON = 0.1


def SARSA(env, num_episodes):
    num_actions = env.action_space.n
    Q = defaultdict(lambda: np.zeros(num_actions))

    def epsilon_greedy_policy(state):
        # A* denotes the optimal action
        A_star = np.argmax(Q[state])
        # handle all non-optimal-action values first
        policy_for_state = np.ones(num_actions, dtype=float) * EPSILON / num_actions
        # optimal-action value
        policy_for_state[A_star] = 1 - EPSILON + EPSILON / num_actions
        return policy_for_state

    episode_lengths = []
    
    for _ in range(num_episodes):  # repeat for each episode
        # initialize S
        cur_state = env.reset()
        length_current_episode = 1
        # choose A from S using a Q derived policy
        action = np.random.choice(np.arange(num_actions), p=epsilon_greedy_policy(cur_state))
        while True:
            # take action, observe reward, nextstate
            nextstate, reward, done, _ = env.step(action)
            length_current_episode += 1
            # choose A' from S' using a Q derived policy
            next_action = np.random.choice(np.arange(num_actions), p=epsilon_greedy_policy(nextstate))
            # TD Update
            Q[cur_state][action] += ALPHA * (reward + GAMMA * Q[nextstate][next_action] - Q[cur_state][action])
            if done:
                break
            action = next_action
            cur_state = nextstate

        episode_lengths.append(length_current_episode)
    
    return Q, episode_lengths

env = gym.make('WindyGridWorld-v0').unwrapped
Q, episode_lengths = SARSA(env, 300)

plt.style.use('grayscale')
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(episode_lengths, label='Episode Lengths')
ax.grid(True)
ax.legend(loc='right')
ax.set_title('Number of actions before termination')
ax.set_xlabel('Episode')
ax.set_ylabel('Number of Actions')

plt.show()
