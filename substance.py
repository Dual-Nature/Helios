# This class only poses electromagnetic properties of substance
# A substance is a matter that has definite properties and composition

# not used now

# default properties
permittivity = 8.854 * 10**(-12) # F/m
permeability = 1.257 * 10**(-6) # H/m

class Substance:
    def __init__(self,name):
        self.name = name
        self.resistivity = 0
        self.permeability = permeability
        self.permittivity = permittivity
        self.volume = 1
        self.surfaceArea = 1
        self.position = [0,0,0]
        self.charge = 0


    def setStructure(self,vol,srfarea):
        self.volume = vol
        self.surfaceArea = srfarea

    def setPosition(self,pos):
        self.position = pos

    def getChargeDensity(self):
        return self.charge/self.volume

    

    def __str__(self):
        return self.name