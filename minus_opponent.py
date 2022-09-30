import random

def minus_opponent(observation, configuration):
    """Returns opponent's last step inferior, first step - 'scissors'"""
    if observation.step > 0:
        return (observation.lastOpponentAction-1) % 3
    else:
        return 2
