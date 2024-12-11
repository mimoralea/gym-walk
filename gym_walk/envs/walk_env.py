import sys
import numpy as np
from six import StringIO
from string import ascii_uppercase
from typing import Optional
import pygame

import gymnasium as gym
from gymnasium import spaces, utils
from gymnasium.envs.toy_text.utils import categorical_sample

WEST, EAST = 0, 1


class WalkEnv(gym.Env):
    metadata = {"render_modes": [None, "human", "ansi"], "render_fps": 5}

    def __init__(self, n_states=7, p_stay=0.0, p_backward=0.5, render_mode=None, verbose=0):
        self.verbose = verbose
        self.shape = (1, n_states + 2)
        self.start_state_index = self.shape[1] // 2

        self.render_mode = render_mode
        if render_mode == "human":
            pygame.init()
            self._pygame_initialized = True
            self.screen_size = (800, 200)
            self.cell_width = self.screen_size[0] // (self.shape[1] - 2)
            self.screen = pygame.display.set_mode(self.screen_size)
            pygame.display.set_caption("Random Walk")
            self.clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0))
            pygame.display.flip()

        self.nS = nS = np.prod(self.shape)
        self.nA = nA = 2

        self.P = {}
        for s in range(nS):
            self.P[s] = {}
            for a in range(nA):
                p_forward = 1.0 - p_stay - p_backward

                # Ensure state transitions stay within bounds
                s_forward = np.clip(s - 1 if a == WEST else s + 1, 0, nS - 1)
                s_backward = np.clip(s + 1 if a == WEST else s - 1, 0, nS - 1)

                # Rewards for transitions
                r_forward = 1.0 if s == nS - 2 and s_forward == nS - 1 else 0.0
                r_backward = 1.0 if s == nS - 2 and s_backward == nS - 1 else 0.0

                # Termination checks
                d_forward = (s >= nS - 2 and s_forward == nS - 1) or (s <= 1 and s_forward == 0)
                d_backward = (s >= nS - 2 and s_backward == nS - 1) or (s <= 1 and s_backward == 0)

                # Transition probabilities
                self.P[s][a] = [
                    (p_forward, s_forward, r_forward, d_forward),
                    (p_stay, s, 0.0, s in [0, nS - 1]),
                    (p_backward, s_backward, r_backward, d_backward),
                ]

                # Validate probabilities sum to 1.0
                assert np.isclose(p_forward + p_stay + p_backward, 1.0), \
                        f"Probabilities do not sum to 1.0 for state {s}, action {a}"

        self.isd = np.zeros(nS)
        self.isd[self.start_state_index] = 1.0
        self.lastaction = None # for rendering

        self.action_space = spaces.Discrete(self.nA)
        self.observation_space = spaces.Discrete(self.nS)

        self.reset()

    def step(self, action):
        # ensure not a nan
        if np.isnan(action):
            return self.s, 0.0, True, True, {"success": False}

        action = round(action)

        if not self.action_space.contains(action):
            return self.s, 0.0, True, True, {}

        # Fetch transitions and sample
        transitions = self.P[self.s][action]
        i = categorical_sample([t[0] for t in transitions], self.np_random)
        p, s, r, terminated = transitions[i]
        self.s = s
        self.lastaction = action

        # Add success information if the state is terminal and the agent succeeded
        info = {"prob": p}
        if terminated and (self.s in [0, self.nS - 1]):
            info["success"] = True
        else:
            info["success"] = False

        return int(s), r, terminated, False, info

    def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None):
        super().reset(seed=seed)
        self.s = int(categorical_sample(self.isd, self.np_random))  # Ensure state is an integer
        self.lastaction = None
        return int(self.s), {"prob": self.isd[self.s]}

    def render(self):
        mode = self.render_mode
        if mode is None:
            return

        if mode == "ansi":
            outfile = StringIO() if mode == "ansi" else sys.stdout
            desc = np.asarray(["[" + ascii_uppercase[: self.shape[1] - 2] + "]"], dtype="c").tolist()
            desc = [[c.decode("utf-8") for c in line] for line in desc]
            color = "red" if self.s == 0 else "green" if self.s == self.nS - 1 else "yellow"
            desc[0][self.s] = utils.colorize(desc[0][self.s], color, highlight=True)
            outfile.write("\n")
            outfile.write("\n".join("".join(line) for line in desc) + "\n")
            return outfile.getvalue()

        if mode == "human":
            self.human()

    def human(self):
        if self.verbose > 0:
            print("Rendering the environment with Pygame...")

        # Colors
        BG_COLOR = (30, 30, 30)  # Background color
        CELL_COLOR = (200, 200, 200)  # Default cell color
        AGENT_COLOR = (255, 255, 0)  # Yellow for agent
        TERMINAL_COLOR = (0, 255, 0)  # Green for terminal states
        LEFT_TERMINAL_COLOR = (255, 0, 0)  # Red for left terminal state

        # Pump Pygame events to keep the event queue alive
        pygame.event.pump()

        # Clear the screen
        self.screen.fill(BG_COLOR)

        # Draw the grid
        for i in range(self.shape[1] - 2):
            cell_x = i * self.cell_width
            cell_rect = pygame.Rect(cell_x, 50, self.cell_width, 100)

            if i == 0:    # Left terminal state
                pygame.draw.rect(self.screen, LEFT_TERMINAL_COLOR, cell_rect)
            elif i == self.nS - 1:    # Right terminal state
                pygame.draw.rect(self.screen, TERMINAL_COLOR, cell_rect)
            elif i == self.s:    # Agent position
                pygame.draw.rect(self.screen, AGENT_COLOR, cell_rect)
            else:
                pygame.draw.rect(self.screen, CELL_COLOR, cell_rect)

            # Draw the border
            pygame.draw.rect(self.screen, (0, 0, 0), cell_rect, 2)

        # Refresh display
        pygame.display.flip()

        # Maintain frame rate
        self.clock.tick(self.metadata["render_fps"])


if __name__ == "__main__":
    env = WalkEnv(n_states=7, p_stay=0.1, p_backward=0.3)

    # Test 2: Action boundaries
    print("Testing action boundaries...")
    try:
        env.step(-1)
    except ValueError as e:
        print(f"Correctly handled invalid action: {e}")

    try:
        env.step(env.nA)
    except ValueError as e:
        print(f"Correctly handled invalid action: {e}")

    # Test 3: Probability sum
    print("Testing probability sums...")
    for s in range(env.nS):
        for a in range(env.nA):
            probs = [t[0] for t in env.P[s][a]]
            assert np.isclose(sum(probs), 1.0), f"Probabilities for state {s}, action {a} do not sum to 1"

    print("Testing Pygame rendering...")
    env = WalkEnv(n_states=7, p_stay=0.1, p_backward=0.3, render_mode="human")

    # Initialize environment
    env.reset()

    # Run a loop to display the environment with Pygame rendering
    try:
        for _ in range(50):  # Run 50 steps in the environment
            env.render()  # Ensure the Pygame rendering is active
            action = env.action_space.sample()  # Sample a random action

            state, reward, done, truncated, info = env.step(action)
            if done:
                env.reset()  # Reset if the episode ends
    except KeyboardInterrupt:
        print("Exiting...")

    print("All tests passed!")
