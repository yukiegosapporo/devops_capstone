import logging
import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2


def test_predict(**kw):
    config = kw["config"]

    env = gym.make('CartPole-v1')
    env = DummyVecEnv([lambda: env])
    model = PPO2(MlpPolicy, env, verbose=1)
    model.load(config["model_path"])

    obs = env.reset()
    for i in range(config["test_epochs"]):
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        logging.info(obs)
        logging.info(rewards)
        logging.info(dones)
        logging.info(info)
        # env.render()
