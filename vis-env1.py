import time
import gym

env = gym.make("CartPole-v0")
env.reset()

for i in range(10000):
    env.render()
    env.step(env.action_space.sample())
    time.sleep(0.1)
    








