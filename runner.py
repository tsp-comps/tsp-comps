from datasets import Datasets

# q: how do we save the results?
# q: are we outputting the intermediary results?

def select_dataset():
    """
    Select a dataset to work on.
    """
    number = input("Select a dataset to work on: 1 for TSP95, 2 for Electrical grid," + 
                   "3 for Protein data.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No dataset selected. Exiting.")

    elif number == "1":

        choice = input("Select a dataset to work on: wi for wi29, uy for uy734, " + 
                   "ca for ca4663.\nEnter the dataset index below: ")
        
        if choice == "wi":
            print("wi29 dataset selected.")
            return Datasets.process_tsp95("datasets/wi29.tsp")

        elif choice == "uy":
            print("uy734 dataset selected.")
            return Datasets.process_tsp95("datasets/uy734.tsp")

        elif choice == "ca":
            print("ca4663 dataset selected.")
            return Datasets.process_tsp95("datasets/ca4663.tsp")

        else:
            print("Invalid dataset index. Exiting.")
            return None

    elif number == "2":
        print("Electric grid dataset selected. This functionality is not yet supported!")

    elif number == "3":
        print("Protein data selected. This functionality is not yet supported!")

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
        print("Christofides algorithm selected. This functionality is not yet supported!")

    elif number == "2":
        print("Nearest Neighbor algorithm selected. This functionality is not yet supported!")

    elif number == "3":
        print("Smallest Insertion Annealing algorithm selected. This functionality is not yet supported!")

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

    return

if __name__=="__main__":
    main()