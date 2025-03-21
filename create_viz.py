from datasets import Datasets
from smallest_insertion import SmallestInsertion
from christofides import Christofides
from nearest_neighbor import NeareastNeighbor
from nearest_neighbor_optimized import NeareastNeighborOptimized
import graphtour_visualization as gv
import tsplib95
import time
import sys

"""
This file creates visualizations for tours based on a file containing a tour and the graph per se
"""

sys.setrecursionlimit(2147483647)

input_file = ""
should_update = False

def select_dataset():
    global input_file
    global should_update
    """
    Select a dataset to work with.
    """
    number = input("Select a dataset to work on: 1 for TSP95, 2 for Electrical grid," + 
                   " 3 for Protein data.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No dataset selected. Exiting.")

    elif number == "1":

        choice = input("Select a dataset to work on: wi for wi29, dj for dj38, qa for qa194, uy for uy734, " + 
                   "zi for zi929, my for mu1979, ca for ca4663, gr for gr9882, fi for fi10639, it for it16862." + 
                   "\nEnter the dataset index below: ")
        options = {"wi": "wi29", "uy": "uy734", "ca": "ca4663", "fi": "fi10639", 
                   "it": "it16862", "dj": "dj38", "qa": "qa194", "zi": "zi929", "my": "mu1979", "gr": "gr9882"}

        input_file += "_"+choice
        
        if choice in options:
            print(f"{options[choice]} dataset selected.")
            file_path = f"datasets/tsp95/{options[choice]}.tsp"
            return [Datasets.process_tsp95(file_path), tsplib95.load(file_path)]

        print("Invalid dataset index. Exiting.")
        return None

    elif number == "2":
        choice = input("Select a dataset to work on: EG for Electric Grid Dataset" + 
                   "\nEnter the dataset index below: ")
        options = {"EG": "electric_points"}

        input_file += "_"+choice
        should_update = True

        if choice in options:
            print(f"{options[choice]} dataset selected.")
            return [Datasets.load_electric_grid_dataset(f"datasets/electric-grid/{options[choice]}.tsv")]

    elif number == "3":
        choice = input("Select a dataset to work on: ALD for Yeast Alcohol Dehydrogenase" + 
                   "\nEnter the dataset index below: ")
        options = {"ALD": "YALD2-n11e45"}

        
        input_file += "_"+choice
        should_update = True
        
        if choice in options:
            print(f"{options[choice]} dataset selected.")
            return [Datasets.load_protein_dataset(f"datasets/proteins/{options[choice]}.tsv")]

        print("Invalid dataset index. Exiting.")
        return None

    else:
        print("Invalid dataset number. Exiting.")
    
    return None

def select_algorithm():
    global input_file
    """
    Select an algorithm to use.
    """
    number = input("Select an algorithm to use: 1 for Christofides, 2 for Nearest Neighbor, " + 
                   "3 for Smallest Insertion, 4 for Nearest Neighbor Optimized.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No algorithm selected. Exiting.")

    elif number == "1":
        print("Christofides algorithm selected.")
        input_file += "_christofides"
        return True

    elif number == "2":
        print("Nearest Neighbor algorithm selected.")
        input_file += "_nearestneighbor"
        return True

    elif number == "3":
        print("Smallest Insertion algorithm selected.")
        input_file += "_smallestinsertion"
        return True

    elif number == "4":
        print("Nearest Neighbor Optimizes algorithm selected.")
        input_file += "_nearestneighboroptimized"
        return True

    else:
        print("Invalid algorithm number. Exiting.")
    
    return False

def visualize_tour(tour, dataset):
    """
    Choose to visualize or not.
    """
    choice = input("Select an algorithm to use: y for Yes, n for No.\nEnter the option below: ") # user input
    
    if len(choice) == 0: 
        print("No algorithm selected. Exiting.")

    elif choice == "y": 
        print("Starting Visualization.")
        if len(dataset) == 2:
            gv.draw_tsp_paths_euclidean(tour, dataset[1])
        else:
            print(type(tour[0]))
            if type(tour[0]) == str:
                gv.draw_tsp_paths_euclidean(tour)
            else:
                gv.draw_tsp_paths_noneuclidean(dataset[0], tour)

    elif choice == "n":
        print("Visuzlization rejected. Exiting.")

    else:
        print("Invalid algorithm number. Exiting.")

def main():
    #Validate selections
    dataset = select_dataset()
    if dataset is None:
        return
    algorithm = select_algorithm()
    if not algorithm:
        return
    #Read solved tour from file 
    tour_file = open("results/tour"+input_file+".txt", "r")
    tour = []
    for line in tour_file:
        line = line.split()
        i = 0
        while i < len(line) and not should_update:
            line[i] = int(line[i])
            i += 1
        tour += line
    print(tour)


    visualize_tour(tour, dataset)

    return

if __name__=="__main__":
    main()
