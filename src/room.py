 #Implement a class to hold room information. This should have name and
 #description attributes.

class Room():
     def __init__(self, name, description, north='', south='', east='', west=''):
        self.name = name
        self.description = description
        self.n_to = north
        self.s_to = south
        self.e_to = east
        self.w_to = west
