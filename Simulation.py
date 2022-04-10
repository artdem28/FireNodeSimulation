from Neighborhood import Neighborhood
import numpy as np


class Simulation:
    """
    This class handles a single run of num_of_iterations years, and the stats for it.
    """

    def __init__(self, desired_statistics, coordinates):
        self.statistics = dict()
        for desired_stat in desired_statistics:
            self.statistics[desired_stat] = list()
        self.coordinates = coordinates

    def run_simulation(self, num_of_iterations, mitigation_level, wind_direction, wind_speed_multiplier):
        neighborhood = Neighborhood(self.coordinates, mitigation_level, wind_direction, wind_speed_multiplier)
        for iteration in range(num_of_iterations):
            neighborhood.simulate_fire()
            desired_vals = neighborhood.data_handler(self.statistics.keys())
            for key in self.statistics.keys():
                if key == "Heatmap":
                    if len(self.statistics[key]) == 0:
                        self.statistics[key] = desired_vals[key]
                    else:
                        self.statistics[key] = np.add(self.statistics[key], desired_vals[key])
                else:
                    self.statistics[key].append(desired_vals[key])
            neighborhood.reset_neighborhood()
        for key in self.statistics.keys():
            if key == "Standard Deviation of # of Affected Houses":
                self.statistics[key] = np.std(self.statistics[key])
            elif key == "Heatmap":
                pass
            else:
                self.statistics[key] = np.mean(self.statistics[key])
        return

    def get_statistics(self):
        return self.statistics
