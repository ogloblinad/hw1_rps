def onetwothree_opponent(observation, configuration):
    """Returns value in cycle (0, 1, 2)"""
    return observation.step % 3 
