from House import House, Edge


class Neighborhood:
    """This class holds all the house objects in the neighborhood and sets up the edges between houses. Simulates
    fire spread and primary fire ignition"""

    def __init__(self, coordinates):
        assert type(coordinates) is list, \
            "Must input a list of coordinate tuples."
        self.houses = self.assign_houses(coordinates)
        self.connect_houses(self.houses)

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
                if house1 != house2:
                    house1.add_edge(Edge(house1, house2))
        return

    '''_______The following functions perform primary fire ignition and fire spread simulation_________'''

    # Starts a primary fire at house 1.
    def first_house_ignition(self):
        self.houses[0].set_state(1)
        return