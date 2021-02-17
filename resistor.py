import numpy as np
from lumpedElement import LumpedElement

class Resistor(LumpedElement):
    def __init__(self,resistance):
        LumpedElement.__init__(2)
        self.resistance = resistance

    def getPotentialDiff(self,i,inverse = False):
        self.current = np.array([[0,i],[-i,0]])
        self.potentialDiff = self.current(-self.resistance)
        if inverse:
            return self.potentialDiff[1][0]
        else:
            return self.potentialDiff[0][1]

    def getCurrent(self,v,t1 = 'a',t2 = 'b'):
        self.potentialDiff = np.array([[0,v],[-v,0]])
        self.current = self.potentialDiff/self.resistance