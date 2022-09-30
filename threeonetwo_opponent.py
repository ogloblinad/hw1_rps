def threeonetwo_opponent(observation, configuration):
    """Returns value in cycle (2, 1, 0)"""
    return (observation.step - 1 )% 3 
