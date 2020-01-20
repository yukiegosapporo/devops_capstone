import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2


def trainer(**kw):
    """
    Trainer func
    """
    config = kw["config"]

    env = gym.make('CartPole-v1')
    env = DummyVecEnv([lambda: env])
    model = PPO2(MlpPolicy, env, verbose=0)
    model.learn(total_timesteps=config["train_epochs"])

    env.close()
    model.save(config["model_path"])
