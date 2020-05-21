 #Implement a class to hold room information. This should have name and
 #description attributes.

class Room():
     def __init__(self, name, description, north= None, south= None, east= None, west= None):
        self.name = name
        self.description = description
        self.n_to = north
        self.s_to = south
        self.e_to = east
        self.w_to = west
        self.items = []

     def list_items(self):
        return ([self.items[i].name for i in range(len(self.items))])
