import time
import numpy as np
from Simulation import Simulation

FIRES_TO_SIMULATE = 1000
HOUSE_COORDINATES = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
                     (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
                     (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
                     (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
                     (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
                     (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9),
                     (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9),
                     (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9),
                     (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9),
                     (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)
                     ]
MITIGATION_LEVEL = 0
WIND_DIRECTION = 0
WIND_SPEED_MULTIPLIER = 0
CSV_file = "simulation_results.csv"
DESIRED_STATS = ["# of Houses Affected by Primary", "# of Houses Affected by Secondary", "Total # of Houses Affected",
                 "Standard Deviation of # of Affected Houses"]


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
    sim.run_simulation(FIRES_TO_SIMULATE, MITIGATION_LEVEL, WIND_DIRECTION, WIND_SPEED_MULTIPLIER)
    store_stats(CSV_file, sim.get_statistics())
    end = time.time()
    print(f"Took {end - start} seconds to run.")
