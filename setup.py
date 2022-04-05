from setuptools import setup

setup(
    name='gym_walk',
    version='0.0.2',
    description='Gym walk environment - useful to replicate Random Walk experiments',
    url='https://github.com/mimoralea/gym-walk',
    author='Miguel Morales',
    author_email='mimoralea@gmail.com',
    packages=['gym_walk', 'gym_walk.envs'],
    license='MIT License',
    install_requires=['gym'],
)
