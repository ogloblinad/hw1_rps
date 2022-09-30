
def even_agent(observation, configuration):
    """Returns 0 and 2 in cycle"""
    return 2*(observation.step % 2)
