import numpy as np


class Edge:
    '''This class respresent the edges betweeen houses. An edge holds the distance and edge angle between two houses.
    Establishes the probability of secondary fire spread between two houses.'''

    def __init__(self, house1, house2, wind_direction, wind_speed_multiplier):
        self.house1 = house1
        self.house2 = house2
        self.mitigation_level = (house1.mitigation_level + house2.mitigation_level) / 2
        self.angle = np.arctan2((house2.y - house1.y), (house2.x - house1.x))
        self.distance = np.sqrt(((house2.x - house1.x) ** 2) + ((house2.y - house1.y) ** 2))

        self.wind_angle = np.radians(wind_direction)
        self.wind_multiplier = 0 if (self.wind_angle - self.angle) <= 0 else \
            np.cos(self.wind_angle - self.angle) * wind_speed_multiplier
        self.distance_probability = .6 if self.distance == 1 else 0
        self.final_probability = (self.distance_probability + self.mitigation_level * (-self.distance_probability)) \
                                 + (self.wind_multiplier * self.distance_probability)

    '''___Getters___'''

    def get_probability(self):
        return self.final_probability
