""" Lumped Element Abstraction"""

import numpy as np

class LumpedElement:
    def __init__(self,n):
        self.terminals = []
        self.setTerminals(n)
        self.nOfTerminals = n
        self.potentialDiff = np.zeros((n,n))
        self.current = np.zeros((n,n))
    
    def setTerminals(self,n):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(n):
            self.terminals.append(alphabet[i])

    def applyPotentialDiffs(self,ar):
        self.potentialDiff = ar

    def applyCurrents(self,ar):
        self.current = ar
    
    def setPotentialDiff(self,value = 0,t1 = 'a',t2 = 'b'):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if t1 in self.terminals and t2 in self.terminals:
            i = alphabet.index(t1)
            j = alphabet.index(t2)
            self.potentialDiff[i][j] = value
            self.potentialDiff[j][i] = -value
        else:
            raise ValueError('given terminal is not present in element')
    
    def setCurrent(self,value = 0,t1 = 'a',t2 = 'b'):
        if t1 in self.terminals and t2 in self.terminals:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            i = alphabet.index(t1)
            j = alphabet.index(t2)
            self.current[i][j] = value
            self.current[j][i] = -value
        else:
            raise ValueError('given terminal is not present in element')
             
    def getPotentialDiff(self,t1 = 'a',t2 = 'b'):
        if t1 in self.terminals and t2 in self.terminals:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            i = alphabet.index(t1)
            j = alphabet.index(t2)
            return self.potentialDiff[i][j]
        else:
            raise ValueError('given terminal is not present in element')

    def getCurrent(self,t1 = 'a',t2 = 'b'):
        if t1 in self.terminals and t2 in self.terminals:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            i = alphabet.index(t1)
            j = alphabet.index(t2)
            return self.current[i][j]
        else:
            raise ValueError('given terminal is not present in element')