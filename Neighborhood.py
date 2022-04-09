from Node import House, Edge
import numpy as np


class Neighborhood:
    """This class holds all the house objects in the neighborhood and sets up the edges between houses. Simulates
    fire spread and primary fire ignition"""

    def __init__(self, coordinates, mitigation_level, wind_direction, wind_speed_multiplier):
        self.mitigation_level = mitigation_level
        assert 360 >= wind_direction >= 0, "Wind direction input must be between 0 and 360 degrees."
        self.wind_direction = wind_direction
        self.wind_speed_multiplier = wind_speed_multiplier
        assert type(coordinates) is list, \
            "Must input a list of coordinate tuples."
        self.houses = self.assign_houses(coordinates, mitigation_level)
        self.connect_houses()
        self.just_on_fire = False

    # Appends Node objects from a list of coordinates
    def assign_houses(self, coords, mitigation_level):
        houses = list()
        i = 1
        for c in coords:
            houses.append(House(i, c, mitigation_level))
        return houses

    # Connects each node object to each other. Grows list of edges in each House object.
    def connect_houses(self):
        houses = self.houses
        for house1 in houses:
            for house2 in houses:
                if house1 is not house2:
                    house1.add_edge(Edge(house1, house2, self.wind_direction, self.wind_speed_multiplier))
        return

    '''_______The following functions perform primary fire ignition and fire spread simulation_________'''

    # Starts a primary fire at house 1.
    def first_house_ignition(self):
        self.houses[0].primary_ignition()
        self.just_on_fire = True
        return

    def neighborhood_burned(self):
        if self.just_on_fire:
            return False
        else:
            for house in self.houses:
                if house.house_state in [1, 2]:
                    return False
            return True

    # Updates all house that were caught on fire to fire spreading state.
    def update_neighborhood(self):
        for house in self.houses:
            house.burns_down()
            if house.caught_primary:
                house.caught_primary = False
                house.house_state = 1
            if house.caught_secondary:
                house.caught_secondary = False
                house.house_state = 2
        return

    # Simulates Fire Spread
    def simulate_fire_spread(self, time_steps=10):
        while not self.neighborhood_burned():
            self.update_neighborhood()
            for house in self.houses:
                if house.is_on_fire():
                    for edge in house.edges:
                        if edge.house2.never_on_fire():
                            if np.random.random() < edge.get_probability():
                                edge.house2.secondary_ignition()
            self.just_on_fire = False
        return

    def simulate_fire(self):
        self.first_house_ignition()
        self.simulate_fire_spread()
        return

    def reset_neighborhood(self):  # resets the neighborhood
        for house in self.houses:
            house.house_state = 0
            house.caught_primary = False
            house.caught_secondary = False
        return

    '''The following function handle data from the simulation'''

    # Statistics handler
    def data_handler(self, desired_data):
        """
        Handles processing of data for a single neighborhood.
        """
        returned_dict = dict()
        if "# of Houses Affected by Primary" in desired_data:
            returned_dict["# of Houses Affected by Primary"] = self.get_num_of_houses_set_alight_by_primary()
        if "# of Houses Affected by Secondary" in desired_data:
            returned_dict["# of Houses Affected by Secondary"] = self.get_num_of_houses_set_alight_by_secondary()
        if "Total # of Houses Affected" in desired_data:
            returned_dict["Total # of Houses Affected"] = self.get_num_of_houses_set_alight()
        if "Standard Deviation of # of Affected Houses" in desired_data:
            returned_dict["Standard Deviation of # of Affected Houses"] = self.get_num_of_houses_set_alight()
        return returned_dict

    def get_num_of_houses_set_alight_by_primary(self):
        num_of_houses = 0
        for house in self.houses:
            if house.house_state in [1, 3]:
                num_of_houses += 1
        return num_of_houses

    def get_num_of_houses_set_alight_by_secondary(self):
        num_of_houses = 0
        for house in self.houses:
            if house.house_state in [2, 4]:
                num_of_houses += 1
        return num_of_houses

    def get_num_of_houses_set_alight(self):
        return self.get_num_of_houses_set_alight_by_primary() + self.get_num_of_houses_set_alight_by_secondary()
