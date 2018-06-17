from gym import envs
import gym
env = gym.make('Blackjack-v0')
env.reset()
for _ in range(1000):
    print(env.step(env.action_space.sample()))
