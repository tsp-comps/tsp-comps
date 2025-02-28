from tour_compare_algorithms import find_longest_consecutive_path, number_of_common_edges

input_file = ""
input_file2 = ""
modify_names = False

def select_dataset():
    global input_file
    global input_file2
    global modify_names
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

        input_file += "_"+choice
        input_file2 += "_"+choice
        return True
        

    elif number == "2":
        choice = input("Select a dataset to work on: EG for Electric Grid Dataset" + 
                   "\nEnter the dataset index below: ")
        options = {"EG": "electric_points"}

        input_file += "_"+choice
        input_file2 += "_"+choice
        modify_names = True
        return True


    elif number == "3":
        choice = input("Select a dataset to work on: ALD for Yeast Alcohol Dehydrogenase" + 
                   "\nEnter the dataset index below: ")
        options = {"ALD": "YALD2-n11e45"}

        input_file += "_"+choice
        input_file2 += "_"+choice
        modify_names = True
        return True
        
        

    else:
        print("Invalid dataset number. Exiting.")
    
    return None

def select_algorithm():
    global input_file
    global input_file2
    """
    Select an algorithm to use.
    """
    number = input("Select the first algorithm to use: 1 for Christofides, 2 for Nearest Neighbor, " + 
                   "3 for Smallest Insertion, 4 for Nearest Neighbor Optimized.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No algorithm selected. Exiting.")
        return True

    elif number == "1":
        print("Christofides algorithm selected.")
        input_file += "_christofides"
        

    elif number == "2":
        print("Nearest Neighbor algorithm selected.")
        input_file += "_nearestneighbor"
        


    elif number == "3":
        print("Smallest Insertion algorithm selected.")
        input_file += "_smallestinsertion"



    elif number == "4":
        print("Nearest Neighbor Optimizes algorithm selected.")
        input_file += "_nearestneighboroptimized"


    else:
        print("Invalid algorithm number. Exiting.")
    
    number = input("Select the second algorithm to use: 1 for Christofides, 2 for Nearest Neighbor, " + 
                   "3 for Smallest Insertion, 4 for Nearest Neighbor Optimized.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No algorithm selected. Exiting.")
        return True

    elif number == "1":
        print("Christofides algorithm selected.")
        input_file2 += "_christofides"
        return True

    elif number == "2":
        print("Nearest Neighbor algorithm selected.")
        input_file2 += "_nearestneighbor"
        return True


    elif number == "3":
        print("Smallest Insertion algorithm selected.")
        input_file2 += "_smallestinsertion"
        return True


    elif number == "4":
        print("Nearest Neighbor Optimizes algorithm selected.")
        input_file2 += "_nearestneighboroptimized"
        return True

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

    tour_file = open("results/tour"+input_file+".txt", "r")
    tour2_file = open("results/tour"+input_file2+".txt", "r")
    tour = []
    tour2 = []
    for line in tour_file:
        line = line.split()
        i = 0
        while i < len(line) and not modify_names:
            line[i] = int(line[i])
            i += 1
        tour += line
    for line in tour2_file:
        line = line.split()
        i = 0
        while i < len(line) and not modify_names:
            line[i] = int(line[i])
            i += 1
        tour2 += line
    if modify_names:
        update_names(tour, tour2)
    longest_consecutive_path = find_longest_consecutive_path(tour.copy(), tour2.copy())
    common_edges  = number_of_common_edges(tour.copy(), tour2.copy())
    print("Largest number of nodes in path both tours have in common is ", longest_consecutive_path)
    print("The number of edges both tours have in common is ", common_edges)


    return


def update_names(tour1, tour2):
    dictionary = {}
    i = 1
    while i < len(tour1):
        dictionary[tour1[i - 1]] = i
        tour1[i - 1] = i
        i += 1
    tour1[i-1] = 1
    j = 0
    while j < len(tour2):
        tour2[j] = dictionary[tour2[j]]
        j += 1
        
if __name__=="__main__":
    main()



    

        