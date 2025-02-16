from datasets import Datasets
from smallest_insertion import SmallestInsertion
from christofides import Christofides
from nearest_neighbor import NeareastNeighbor

# q: how do we save the results?
# q: are we outputting the intermediary results?

def select_dataset():
    """
    Select a dataset to work on.
    """
    number = input("Select a dataset to work on: 1 for TSP95, 2 for Electrical grid," + 
                   " 3 for Protein data.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No dataset selected. Exiting.")

    elif number == "1":

        choice = input("Select a dataset to work on: wi for wi29, uy for uy734, " + 
                   "ca for ca4663.\nEnter the dataset index below: ")
        options = {"wi": "wi29", "uy": "uy734", "ca": "ca4663"}
        
        if choice in options:
            print(f"{options[choice]} dataset selected.")
            return Datasets.process_tsp95(f"datasets/tsp95/{options[choice]}.tsp")

        print("Invalid dataset index. Exiting.")
        return None

    elif number == "2":
        print("Electric grid dataset selected. This functionality is not yet supported!")

    elif number == "3":
        choice = input("Select a dataset to work on: ALD for Yeast Alcohol Dehydrogenase" + 
                   "\nEnter the dataset index below: ")
        options = {"ALD": "YALD2-n11e45"}
        
        if choice in options:
            print(f"{options[choice]} dataset selected.")
            return Datasets.load_protein_dataset(f"datasets/proteins/{options[choice]}.tsv")

        print("Invalid dataset index. Exiting.")
        return None

    else:
        print("Invalid dataset number. Exiting.")
    
    return None

def select_algorithm():
    """
    Select an algorithm to use.
    """
    number = input("Select an algorithm to use: 1 for Christofides, 2 for Nearest Neighbor, " + 
                   "3 for Smallest Insertion.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No algorithm selected. Exiting.")

    elif number == "1":
        print("Christofides algorithm selected.")
        return Christofides()

    elif number == "2":
        print("Nearest Neighbor algorithm selected.")
        return NeareastNeighbor()

    elif number == "3":
        print("Smallest Insertion algorithm selected.")
        return SmallestInsertion()

    else:
        print("Invalid algorithm number. Exiting.")
    
    return None

def main():

    dataset = select_dataset()
    if dataset is None:
        return
    algorithm = select_algorithm()
    if algorithm is None:
        return
    print("The distance tour is " +str(algorithm.solve(dataset)))

    return

if __name__=="__main__":
    main()
