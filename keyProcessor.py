from __future__ import division, print_function
from random import randrange, getrandbits

import random
import functools





class taskForce:
    
    def isPrime(candidate, multiplier):
        
        if candidate in [2, 3]:
            return True
        
        if candidate <= 1 or candidate % 2 == 0:
            return False
        
        