import tensorflow as tf
import numpy as np
import gym
import logging

logger = logging.getLogger('rl')
logger.setLevel(logging.DEBUG)


class Harness:

    def run_episode(self, env, agent):
        observation = env.reset()
        total_reward = 0
        for _ in range(1000):
            action = agent.next_action(observation)
            observation, reward, done, info = env.step(action)
            total_reward += reward
            if done:
                break
        return total_reward


class LinearAgent:

    def __init__(self):
        self.parameters = np.random.rand(4) * 2 - 1

    def next_action(self, observation):
        return 0 if np.matmul(self.parameters, observation) < 0 else 1


def random_search():
    # implement this!
    best_params = None
    best_reward = -1
    harness = Harness()
    
    env = gym.make("CartPole-v0")

    for i in range(100):
        env.reset()
        agent = LinearAgent()
        reward = harness.run_episode(env, agent)
        if reward > best_reward:
            best_reward = reward
            best_params = agent.parameters
            print("best reward = %s" % best_reward)
            print("best params = %s" % best_params)



random_search()