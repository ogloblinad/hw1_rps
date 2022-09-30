from datetime import datetime 

def time_agent(observation, configuration):
    """Returns remainder of 3 from difference of function creation and execution time"""
    then = datetime(2022, 9, 30, 22, 45, 15)        # Random date in the past
    now  = datetime.now()                         # Now
    dur = (now - then).total_seconds() 
    return round(dur) % 3
