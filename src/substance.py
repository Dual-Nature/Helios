# default properties of vacuum
name = 'space'
resistivity = 0 # ohm*m
permittivity = 8.854 * 10**(-12) # F/m
permeability = 1.257 * 10**(-6) # H/m


class Substance:
    def __init__(self):
        self.name = name
        self.resistivity = resistivity
        self.permeability = permeability
        self.permittivity = permittivity
        self.charge = 0

    def __str__(self):
        return self.name