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
        self.just_on_fire = False
        self.spreading_fire = False

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

    def get_state(self):
        return self.house_state

    '''___Setters___'''
    def add_edge(self, edge):
        self.edges.append(edge)
        return

    def set_state(self, house_state):
        assert house_state in [0, 1, 2, 3, 4], \
            f"Expected combustion state in [0, 1, 2, 3, 4] but got {house_state}."
        self.house_state = house_state
        return

    '''___Fire_State_Functions___'''
    def primary_ignition(self):
        self.house_state = 1
        return

    def secondary_ignition(self):
        self.house_state = 2
        return

    def burns_down(self):
        if self.house_state == 1:
            self.house_state = 3
        else:
            self.house_state = 4
        return

    def reset(self):
        self.house_state = 0
        return

    def is_on_fire(self):
        return self.house_state in [1, 2]

    def is_spreading_fire(self):
        spread_fire = False
        if not self.just_on_fire:
            if self.house_state in [1,2]:
                spread_fire = True
            else:
                spread_fire = False
                self.burns_down()
        return spread_fire

    def update_house(self):
        self.just_on_fire = False

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

    '''___Getters___'''
    def get_probability(self):
        return self.probability


