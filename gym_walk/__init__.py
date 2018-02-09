import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='WalkFiveStates-v0',
    entry_point='gym_walk.envs:WalkFiveStatesEnv',
    timestep_limit=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkTwentyOneStates-v0',
    entry_point='gym_walk.envs:WalkTwentyOneStatesEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)
