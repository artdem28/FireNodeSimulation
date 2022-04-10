class House:
    '''
    The node class represents a house and its connections to other houses. The node itself holds the state of the
    house, such as its property value, mitigation level, other parameters. Each node has a list of edges to other
    houses as well as its state. A house state can be 0: not on fire, 1: on fire from primary, 2: on fire from
    secondary, 3: burned down from primary, 4: burned down from secondary.
    '''

    def __init__(self, house_num, coordinate, mitigation_level):
        self.number = house_num
        self.x = coordinate[0]
        self.y = coordinate[1]
        self.mitigation_level = mitigation_level
        self.edges = list()
        self.house_state = 0
        self.caught_primary = False
        self.caught_secondary = False

    '''___Getters___'''

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

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
        self.caught_primary = True
        return

    def secondary_ignition(self):
        self.caught_secondary = True
        return

    def burns_down(self):
        if self.house_state == 1:
            self.house_state = 3
        elif self.house_state == 2:
            self.house_state = 4
        return

    def reset(self):
        self.house_state = 0
        return

    def is_on_fire(self):
        return self.house_state in [1, 2]

    def never_on_fire(self):
        return self.house_state == 0

