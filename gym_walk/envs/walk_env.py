import sys
import numpy as np
from six import StringIO, b
from string import ascii_uppercase

from gym import utils
from gym.envs.toy_text import discrete

LEFT, RIGHT = 0, 1

class WalkEnv(discrete.DiscreteEnv):

    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self, n_states=5):

        self.shape = (1, n_states + 1)
        self.start_state_index = self.shape[1]//2 - 1

        self.nS = nS = np.prod(self.shape)
        self.nA = nA = 2

        P = {}
        for s in range(nS):
            P[s] = {}
            for a in range(nA):
                prob = 1.0
                new_state = s - 1 if a == LEFT else s + 1
                new_state = nS - 1 if new_state < 0 or s == nS - 1 else new_state
                reward = 1.0 if s == nS - 2 and new_state == nS - 1 else 0.0
                is_terminal = s == nS - 1 and new_state == nS - 1
                P[s][a] = [(prob, new_state, reward, is_terminal)]

        isd = np.zeros(nS)
        isd[self.start_state_index] = 1.0

        discrete.DiscreteEnv.__init__(self, nS, nA, P, isd)

    def render(self, mode='human'):
        outfile = StringIO() if mode == 'ansi' else sys.stdout
        desc = np.asarray([ascii_uppercase[:self.shape[1]-1]], dtype='c').tolist()
        desc = [[c.decode('utf-8') for c in line] for line in desc]
        color = 'red' if self.s == self.nS - 1 and self.lastaction == LEFT else 'yellow'
        color = 'green' if self.s == self.nS - 1 and self.lastaction == RIGHT else color
        s = 0 if self.s == self.nS - 1 and self.lastaction == LEFT else self.s
        s = self.nS - 2 if self.s == self.nS - 1 and self.lastaction == RIGHT else s
        desc[0][s] = utils.colorize(desc[0][s], color, highlight=True)
        outfile.write("\n")
        outfile.write("\n".join(''.join(line) for line in desc)+"\n")

        if mode != 'human':
            return outfile
