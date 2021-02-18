import numpy as np
import matplotlib.pyplot as plt
from lumpedElement import LumpedElement

class Resistor(LumpedElement):
    def __init__(self,resistance):
        super().__init__(2)
        self.resistance = resistance

    def setPotentialDiff(self, value, t1, t2):
        super().setPotentialDiff(value=value, t1=t1, t2=t2)
    
    def setCurrent(self, value, t1, t2):
        super().setCurrent(value=value, t1=t1, t2=t2)
    
    def getPotentialDiff(self, t1, t2):
        self.potentialDiff = self.current*(-1*self.resistance)
        
        

r = Resistor(3)
print(r.getPotentialDiff())