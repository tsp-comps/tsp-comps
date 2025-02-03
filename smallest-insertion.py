import tsplib95
import networkx as nx

# q: how do we save the results?
# q: are we outputting the intermediary results?

def process_tsp95(file_path):
    tsp_set = tsplib95.load(file_path)
    g_tsp = tsp_set.get_graph()
    return g_tsp

def main():

    number = input("Select a dataset to work on: 1 for TSP95, 2 for Electrical grid," + 
                   "3 for Protein data.\nEnter the number below: ") # user input
    
    if len(number) == 0: 
        print("No dataset selected. Exiting.")
    elif number == "1":

        choice = input("Select a dataset to work on: wi for wi29, uy for uy734," + 
                   "ca for ca4663.\nEnter the dataset index below: ")
        
        if choice == "wi":
            print("wi29 dataset selected.")
            g_wi = process_tsp95('datasets/tsp95/wi29.tsp')
            print(nx.approximation.traveling_salesman_problem(g_wi))

        elif choice == "uy":
            print("uy734 dataset selected.")
            g_uy = process_tsp95('datasets/tsp95/uy734.tsp')
            print(nx.approximation.traveling_salesman_problem(g_uy))

        elif choice == "ca":
            print("ca4663 dataset selected.")
            g_ca = process_tsp95('datasets/tsp95/ca4663.tsp')
            print(nx.approximation.traveling_salesman_problem(g_ca))

        else:
            print("Invalid dataset index. Exiting.")

    elif number == "2":
        print("Electric grid dataset selected.")
    elif number == "3":
        print("Protein data selected.")
    else:
        print("Invalid dataset number. Exiting.")

    return

if __name__=="__main__":
    main()