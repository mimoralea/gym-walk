from gym.envs.registration import register

register(
    id='WalkFiveStates-v0',
    entry_point='gym_walk.envs:WalkEnv',
    kwargs={'n_states': 5},
    timestep_limit=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkTwentyOneStates-v0',
    entry_point='gym_walk.envs:WalkEnv',
    kwargs={'n_states': 21},
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)
