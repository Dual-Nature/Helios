from lumpedElement import LumpedElement

class Resistor(LumpedElement):
    def __init__(self,resistance):
        super().__init__(2)
        self.resistance = resistance

    def getPotentialDiff(self, t1 = 1, t2 = 2):
        self.potentialDiff = (-1)*self.resistance*self.current
        return self.potentialDiff[t1-1][t2-1]

    def getCurrent(self, t1 = 1, t2 = 2):
        try:
            self.current = (-1)*self.potentialDiff/self.resistance
            self.current[t1-1][t2-1]
        except ZeroDivisionError:
            raise ValueError('resistance is zero')
    
    def tempEffect(self,temp,tempCoff):
        defaultTemp = 25 # in *C
        self.resistance = self.resistance(1 + tempCoff*(temp - defaultTemp))