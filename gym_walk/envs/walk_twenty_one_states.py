from gym_walk.envs.walk_env import WalkEnv
import numpy as np

class WalkTwentyOneStatesEnv(WalkEnv):
    def __init__(self, bandits=10):
        p_dist = np.random.uniform(size=bandits)
        r_dist = np.random.uniform(size=bandits)
        WalkEnv.__init__(self, p_dist=p_dist, r_dist=r_dist)
