import sys
import numpy as np
from gym import error, spaces
from gym.envs.toy_text import discrete
from gym.utils import seeding

LEFT, RIGHT = 0, 1


class WalkEnv(discrete.DiscreteEnv):

    def __init__(self):

        self.shape = (1, 5)
        self.start_state_index = self.shape[1]//2

        nS = np.prod(self.shape)
        nA = 2

        P = {}
        for s in range(nS):
            P[s] = {}
            for a in range(nA):
                prob = 1.0
                new_state = np.clip(s - 1 if a == LEFT else s + 1, 0, nS - 1)
                new_state = s if s == 0 or s == nS - 1 else new_state
                reward = 1.0 if new_state == nS - 1 else 0.0
                is_terminal = new_state == 0 or new_state == nS - 1
                P[s][a] = (prob, new_state, reward, is_terminal)

        isd = np.zeros(nS)
        isd[self.start_state_index] = 1.0

        super(WalkEnv, self).__init__(nS, nA, P, isd)
