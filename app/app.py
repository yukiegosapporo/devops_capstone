import logging
import gym

from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.policies import MlpPolicy
from stable_baselines import PPO2
from flask import Flask, jsonify
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app=app,
          title="CartPole app",
          description="Dead simple cartpole RL app")

env = gym.make('CartPole-v1')
env = DummyVecEnv([lambda: env])
model = PPO2(MlpPolicy, env, verbose=1)
model.load("model")
obs = env.reset()

@api.route('/')
class HealthCheck(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        """Health check

        :return: health check message
        :rtype: json
        """
        return jsonify({'Message': 'App up and running'})


@api.route('/play')
class Play(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        """Play a RL model with one random epoch

        :return: action value, either 0 or 1
        :rtype: json
        """
        action, _ = model.predict(obs)

        rv = {}
        rv["Action"] = int(action[0])
        logging.info(rv)
        return jsonify(rv)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
