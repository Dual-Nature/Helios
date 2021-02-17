""" Lumped Element Abstraction"""

import numpy as np

class LumpedElement:
    def __init__(self,n = 2):
        self.terminals = []
        self.setTerminals(n)
        self.nOfTerminals = n
        self.potentialDiff = np.zeros((n,n))
        self.current = np.zeros((n,n))
    
    def setTerminals(self,n):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(n):
            self.terminals.append(alphabet[i])
    
    def setPotentialDiff(self,value = 0,t1 = 'a',t2 = 'b'):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        i = alphabet.index(t1)
        j = alphabet.index(t2)
        self.potentialDiff[i][j] = value
        self.potentialDiff[j][i] = -value
    
    def setCurrent(self,value = 0,t1 = 'a',t2 = 'b'):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        i = alphabet.index(t1)
        j = alphabet.index(t2)
        self.current[i][j] = value
        self.current[j][i] = -value
             

l = LumpedElement(3)
l.setPotentialDiff(2)
print(l.potentialDiff)