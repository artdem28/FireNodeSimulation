import numpy as np

class House:
    '''
    The node class represents a house and its connections to other houses. The node itself holds the state of the
    house, such as its property value, mitigation level, other parameters. Each node has a list of edges to other
    houses as well as its state. A house state can be 0: not on fire, 1: on fire from primary, 2: on fire from
    secondary, 3: burned down from primary, 4: burned down from secondary.
    '''
    def __init__(self, house_num, coordinate, property_value = 0, mitigation_level = 0):
        self.number = house_num
        self.x = coordinate[0]
        self.y = coordinate[1]
        self.property_value = property_value
        self.mitigation_level = mitigation_level
        self.edges = list()
        self.house_state = 0

    '''___Getters___'''
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_property_value(self):
        return self.property_value

    def get_mitigation_level(self):
        return self.mitigation_level

    def get_edges(self):
        return self.edges

    '''___Setters___'''
    def add_edge(self, edge):
        self.edges.append(edge)
        return

    def set_state(self, state):
        self.state = state
        return

class Edge:
    '''This class respresent the edges betweeen houses. An edge holds the distance and edge angle between two houses.
    Establishes the probability of secondary fire spread between two houses.'''
    def __init__(self, house1, house2):
        self.distance = np.sqrt((house2.x-house1.x)^2+(house2.y-house1.y)^2)
        self.angle = np.arctan((house2.y-house1.y)/(house2.x-house1.x))
        #just did a curve fit on the probabilities of fire spread based on house seperation
        self.probability = 0.07965812 + (0.9024374 - 0.07965812)/(1 + (self.distance/7.043069)^3.402191)
        self.vegetation_bonus = 0
        self.mitigation_bonus = 0



