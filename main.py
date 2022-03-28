import time
import numpy as np
from Simulation import Simulation

FIRES_TO_SIMULATE = 10000
HOUSE_COORDINATES = [(0,0), (0,1), (0,2), (0,3), (0,4)]
CSV_file = "simulation_results.csv"
DESIRED_STATS = ["# of Houses Affected by Primary", "# of Houses Affected by Secondary", "Total # of Houses Affected"]


def store_stats(csv_file, stats_dict):
    file = open(csv_file, "w")
    for stat in stats_dict.keys():
        file.write(f",{stat}")
    file.write("\n")
    for stat in stats_dict.keys():
        file.write(f",{stats_dict.get(stat)}")
    file.close()
    return


if __name__ == '__main__':
    """ 
    This is the main function for the fire spread model simulation. It will run through simulations with
        varied parameters and calculate some statistics from the results.
    """
    start = time.time()
    print("Running Simulation")
    sim = Simulation(DESIRED_STATS, HOUSE_COORDINATES)
    sim.run_simulation(FIRES_TO_SIMULATE)
    store_stats(CSV_file, sim.get_statistics())
    end = time.time()
    print(f"Took {end - start} seconds to run.")
