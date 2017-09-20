import settings
from random import randint
import numpy as np

###############################################################################
def set_active_state(prob):

    for i in range(0,len(settings.nodesList)):
        #if settings.nodesList[i].sleep_time >0:
        p = randint(0, 100)
        if p < prob:
             settings.nodesList[i].active_state(1) #80% of nodes active
        else:
             settings.nodesList[i].active_state(0)

###############################################################################
             

             
             



