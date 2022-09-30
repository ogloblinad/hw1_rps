def twothreeone_opponent(observation, configuration):
    """Returns value in cycle (1, 2, 0)"""
    return (observation.step - 2 )% 3 
