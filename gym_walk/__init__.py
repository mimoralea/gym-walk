from gym.envs.registration import register


# classics
register(
    # five non-terminal states and two terminal
    # same as below
    id='RandomWalk-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 5, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # five non-terminal states and two terminal
    # same as above
    id='RandomWalkFive-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 5, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # Nineteen non-terminal states and two terminal
    # same as below
    id='RandomWalkLarge-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 19, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # Nineteen non-terminal states and two terminal
    # same as above
    id='RandomWalkNineteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 19, 'p_stay': 0.0, 'p_backward': 0.5},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # One non-terminal states and two terminal
    # Technically speaking, this is a bandit MDP
    id='BanditWalk-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 1, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # One non-terminal states and two terminal
    # Technically speaking, this is a bandit MDP
    id='BanditDeterministicWalk-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 1, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    # One non-terminal states and two terminal
    # Technically speaking, this is a bandit MDP
    id='BanditSlipperyWalk-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 1, 'p_stay': 0.0, 'p_backward': 0.2},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)

# deterministic transition walks
register(
    id='WalkThree-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 3, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
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
    id='WalkFifthteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 15, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='WalkSeventeen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 17, 'p_stay': 0.0, 'p_backward': 0.0},
    max_episode_steps=1000,
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

# stochastic transition walks
register(
    id='SlipperyWalkThree-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 3, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='SlipperyWalkFive-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 5, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='SlipperyWalkSeven-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 7, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='SlipperyWalkFifthteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 15, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='SlipperyWalkSeventeen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 17, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=1000,
    reward_threshold=1.0,
    nondeterministic=True,
)
register(
    id='SlipperyWalkNineteen-v0',
    entry_point='gym_walk.envs:WalkEnv',
    # left-most and right-most states are terminal
    kwargs={'n_states': 19, 'p_stay': 0.5*2/3., 'p_backward': 0.5*1/3.},
    max_episode_steps=100,
    reward_threshold=1.0,
    nondeterministic=True,
)
