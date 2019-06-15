from gym.envs.registration import register

register(
    id='WalkFive-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 5, 'noise': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkSeven-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 7, 'noise': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkNine-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 9, 'noise': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkFifthteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 15, 'noise': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkNineteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 19, 'noise': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkTwentyOne-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 21, 'noise': 0.0},
    max_episode_steps=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)

# Noisy walks
register(
    id='NoisyWalkFive-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 5, 'noise': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkSeven-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 7, 'noise': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkNine-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 9, 'noise': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkFifthteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 15, 'noise': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkNineteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 19, 'noise': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkTwentyOne-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 21, 'noise': 0.5},
    max_episode_steps=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)
