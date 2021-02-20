from lumpedElement import LumpedElement

class Capacitor(LumpedElement):
    def __init__(self, capacitance):
        super().__init__(n = 2)
        self.capacitance = capacitance

    def getCurrent(self, t1 = 1, t2 = 2):
        self.current = self.capacitance*