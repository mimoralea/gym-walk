from gym_walk.envs.walk_env import WalkEnv
import numpy as np

class WalkFiveStatesEnv(WalkEnv):
    def __init__(self, bandits=10):
        p_dist = np.random.uniform(size=bandits)
        r_dist = np.full(bandits, 1)
        WalkEnv.__init__(self, p_dist=p_dist, r_dist=r_dist)
