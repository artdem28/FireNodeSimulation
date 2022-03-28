from Neighborhood import Neighborhood

class Simulation:
    """
    This class handles a single run of num_of_iterations years, and the stats for it.
    """

    def __init__(self, desired_statistics, coordinates):
        self.statistics = dict()
        for desired_stat in desired_statistics:
            self.statistics[desired_stat] = list()
        self.coordinates = coordinates
        return

    def run_simulation(self, num_of_iterations):
        for iteration in range(num_of_iterations):
            current_neighborhood = Neighborhood(self.coordinates)
            current_neighborhood.simulate_fire()
            desired_data = self.statistics.keys()
            desired_vals = current_neighborhood.data_handler(desired_data)
            for key in self.statistics:
                self.statistics[key].append(desired_vals[key])
        return

    def get_statistics(self):
        return self.statistics