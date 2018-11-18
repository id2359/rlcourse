# simple agent

import time
import gym

env = gym.make("CartPole-v0")
env.reset()


for i in range(10000):
    env.render()
    action = env.action_space.sample()
    print(action)
    obs, reward, is_done, info = env.step(action)
    print(str(obs))
    print(str(reward))
    time.sleep(1)