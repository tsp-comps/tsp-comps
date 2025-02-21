from datasets import Datasets
from smallest_insertion import SmallestInsertion
from christofides import Christofides

"""
For reproducing the timing results, run it as runner.py < input_data.txt
"""

def select_dataset():
    """
    Select a dataset to work on.
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
        print("Nearest Neighbor algorithm selected. This functionality is not yet supported!")

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