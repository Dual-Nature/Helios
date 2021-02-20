""" Lumped Element Abstraction """

import numpy as np

class LumpedElement:
    def __init__(self,n):
        self.terminalCount = n
        # setting initial current and potential difference to zero
        complexZeros = [complex(0) for _ in range(n*n)]
        self.potentialDiff = np.array(complexZeros).reshape(n,n)
        self.current = np.array(complexZeros).reshape(n,n)

    def setPotentialDiffs(self,ar):
        self.potentialDiff = ar

    def setCurrents(self,ar):
        self.current = ar
    
    def applyPotentialDiff(self,value,t1,t2):
        # value is complex number
        if t1 <= self.terminalCount and t2 <= self.terminalCount:
            self.potentialDiff[t1-1][t2-1] = value
            self.potentialDiff[t2-1][t1-1] = -value
        else:
            raise ValueError('invalid terminal')
    
    def applyCurrent(self,value,t1,t2):
        if t1 <= self.terminalCount and t2 <= self.terminalCount:
            self.current[t1-1][t2-1] = value
            self.current[t2-1][t1-1] = -value
        else:
            raise ValueError('invalid terminal')
             
    def getPotentialDiff(self,t1,t2):
        if t1 <= self.terminalCount and t2 <= self.terminalCount:
            return self.potentialDiff[t1-1][t2-1]
        else:
            raise ValueError('invalid terminal')

    def getCurrent(self,t1,t2):
        if t1 <= self.terminalCount and t2 <= self.terminalCount:
            return self.current[t1-1][t2-1]
        else:
            raise ValueError('invalid terminal')