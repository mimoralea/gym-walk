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

        self.shape = (1, n_states)
        self.start_state_index = self.shape[1]//2

        self.nS = nS = np.prod(self.shape)
        self.nA = nA = 2

        P = {}
        for s in range(nS):
            P[s] = {}
            for a in range(nA):
                prob = 1.0
                new_state = np.clip(s - 1 if a == LEFT else s + 1, 0, nS - 1)
                new_state = s if s == 0 or s == nS - 1 else new_state
                reward = 1.0 if new_state == nS - 1 and s != new_state else 0.0
                is_terminal = new_state == 0 or new_state == nS - 1
                P[s][a] = [(prob, new_state, reward, is_terminal)]

        isd = np.zeros(nS)
        isd[self.start_state_index] = 1.0

        discrete.DiscreteEnv.__init__(self, nS, nA, P, isd)

    def render(self, mode='human', close=False):
        outfile = StringIO() if mode == 'ansi' else sys.stdout
        desc = np.asarray(ascii_uppercase[:self.shape[1]], dtype='c').tolist()
        desc = [[c.decode('utf-8') for c in line] for line in desc]
        color = 'red' if self.s == 0 else 'green' if self.s == self.nS - 1 else 'yellow'
        desc[0][self.s] = utils.colorize(desc[0][self.s], color, highlight=True)
        outfile.write("\n")
        outfile.write("\n".join(''.join(line) for line in desc)+"\n")

        if mode != 'human':
            return outfile
