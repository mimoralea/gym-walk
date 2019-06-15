from gym.envs.registration import register


# classic implementations
register(
    # five non-terminal states and two terminal
    # same as below
    id='RandomWalk-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 7, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # five non-terminal states and two terminal
    # same as above
    id='RandomWalkSeven-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 7, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # Nineteen non-terminal states and two terminal
    id='RandomWalkTwentyOne-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 21, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)

# deterministic transition walks
register(
    id='WalkFive-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 5, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkSeven-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 7, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkNine-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 9, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkFifthteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 15, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkNineteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 19, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkTwentyOne-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 21, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)

# stochastic transition walks
register(
    id='NoisyWalkFive-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 5, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkSeven-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 7, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkNine-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 9, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkFifthteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 15, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkNineteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 19, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='NoisyWalkTwentyOne-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 21, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)
