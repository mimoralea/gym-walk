# gym-walk

## Installation

```bash
git clone https://github.com/mimoralea/gym-walk.git
cd gym-walk
pip install .
```

or:

```bash
pip install git+https://github.com/mimoralea/gym-walk#egg=gym-walk
```

## Use

```python
import gym, gym_walk, numpy as np
env = gym.make('WalkFive-v0')
pi = lambda x: np.random.randint(2)

def td(pi, env, gamma=1.0, alpha=0.01, n_episodes=100000):
    V = np.zeros(env.observation_space.n)
    for t in range(n_episodes):
        state, done = env.reset(), False
        while not done:
            action = pi(state)
            next_state, reward, done, _ = env.step(action)
            td_target = reward + gamma * V[next_state]
            td_error = td_target - V[state]
            V[state] = V[state] + alpha * td_error
            state = next_state
    return V

V = td(pi, env)
V
```
