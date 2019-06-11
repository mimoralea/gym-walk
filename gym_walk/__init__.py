from gym.envs.registration import register

register(
    id='WalkFive-v0',
    entry_point='gym_walk.envs:WalkEnv',
    kwargs={'n_states': 5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkSeven-v0',
    entry_point='gym_walk.envs:WalkEnv',
    kwargs={'n_states': 7},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkTwentyOne-v0',
    entry_point='gym_walk.envs:WalkEnv',
    kwargs={'n_states': 21},
    max_episode_steps=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)
