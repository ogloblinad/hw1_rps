import random

def plus_opponent(observation, configuration):
    """Returns opponent's last step counter, first step - 'rock'"""
    if observation.step > 0:
        return (observation.lastOpponentAction+1) % 3 #stay inside [0,1,2]
    else:
        return 0
