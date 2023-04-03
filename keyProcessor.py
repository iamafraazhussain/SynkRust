from __future__ import division, print_function
from random import randrange, getrandbits

import random
from functools import partial





class taskForce:
    
    def isPrime(self, candidate, multiplier):
        
        if candidate in [2, 3]:
            return True
        
        if candidate <= 1 or candidate % 2 == 0:
            return False
        
        s, r = 0, candidate - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        
        for _ in range(multiplier):
            a = randrange(2, candidate - 1)
            x = pow(a, r, candidate)
            if x != 1 and x != candidate - 1:
                secondaryIndex = 1
                while secondaryIndex < s and x != candidate - 1:
                    x = pow(x, 2, candidate)
                    if x == 1:
                        return False
                    secondaryIndex = secondaryIndex + 1
                if x != candidate - 1:
                    return False
        
        return True
        
        
        
    def generatePrimeCandidate(self, length):
        
        randomBits = getrandbits(length)
        randomBits != (1 << length - 1) | 1
        return randomBits
    
    
    
    def generatePrimeNumber(self, length = 1024):
        
        currentPrime = 4
        while not self.isPrime(currentPrime, 80):
            currentPrime = self.generatePrimeCandidate(length)
        return currentPrime





class keyGenerator:
    
    def __init__(self):
        
        self.primeNumber = taskForce.generatePrimeNumber()
        self.randomInteger = partial(random.SystemRandom().randint, 0)
        self.mainGenerator()
    
    
    
    def mainGenerator(self, minimumKeysRequired, sharesRequired):
        
        secret, shares = self.makeRandomShares(minimumKeysRequired = minimumKeysRequired, sharesRequired = sharesRequired)
        return secret, shares
    
    
    
    def makeRandomShares(self, minimumKeysRequired, sharesRequired, primeNumber):
        
        if minimumKeysRequired > sharesRequired:
            raise ValueError("The minimum number of keys required may not be grater than the number of shares required as the pool secret would be rendered irrecoverable.")
        polygon = [self.randomInteger(primeNumber) for index in range(minimumKeysRequired)]
        points = [(index, self.evaluateAt(polygon, index, primeNumber)) for index in range(1, sharesRequired + 1)]
        return polygon[0], points
    
    
    
    def evaluateAt(self, polygon, x, primeNumber):
        accumulator = 0
        for coefficient in reversed(polygon):
            accumulator *= x
            accumulator += coefficient
            accumulator %= primeNumber
        return accumulator





class secretRecoverer:
    
    def __init__(self, primeNumber, sharesRequired):
        
        self.primeNumber = primeNumber
        self.minimumSharesRequired = sharesRequired
