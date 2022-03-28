from House import House, Edge
import numpy as np


class Neighborhood:
    """This class holds all the house objects in the neighborhood and sets up the edges between houses. Simulates
    fire spread and primary fire ignition"""

    def __init__(self, coordinates):
        assert type(coordinates) is list, \
            "Must input a list of coordinate tuples."
        self.houses = self.assign_houses(coordinates)
        self.connect_houses()

    # Appends Node objects from a list of coordinates
    def assign_houses(self, coords):
        houses = list()
        i = 1
        for c in coords:
            houses.append(House(i, c))
        return houses

    # Connects each node object to each other. Grows list of edges in each House object.
    def connect_houses(self):
        houses = self.houses
        for house1 in houses:
            for house2 in houses:
                if house1 is not house2:
                    house1.add_edge(Edge(house1, house2))
        return

    '''_______The following functions perform primary fire ignition and fire spread simulation_________'''

    # Starts a primary fire at house 1.
    def first_house_ignition(self):
        self.houses[0].set_state(1)
        return

    # Simulates Fire Spread
    def simulate_fire_spread(self, time_steps=7):
        for _ in range(time_steps):
            for house in self.houses:
                if house.is_spreading_fire():
                    for edge in house.edges:
                        if np.random.random() < edge.probability:
                            house.update_house()
                            edge.house2.secondary_ignition()
        return

    def simulate_fire(self):
        self.first_house_ignition()
        self.simulate_fire_spread()
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
