#Two pointer algorithm to count the number of edges
def number_of_common_edges(tour1, tour2):
    #One pointer is always behind the other by 1
    i = 0
    j = 1
    edges = set()
    #While the second pointer isn't by the end of the array, we keep iterating
    #Here we are saving the nodes of the first graph in a set
    while j < len(tour1):
        edges.add((tour1[i], tour1[j]))
        i += 1
        j += 1
    #This is a similar two pointer algorithm, so one pointer is always behind another by 1
    i = 0
    common_edges = 0
    j = 1
    #Counts how many edges both tours have in common
    while j < len(tour2):
        if (tour2[i], tour2[j]) in edges:
            common_edges += 1
        i += 1
        j += 1
    return common_edges


#As the tour is a cycle, this makes the edge we are currently at the beginning of the tour. 
def array_splicer(target_number, tour):
    order_starting_from_target_number = []
    order_before_target_number = []
    i = 0
    #Everything before the node we are currently at gets processed here
    while True:
        if tour[i] == target_number:
            break
        order_before_target_number.append(tour[i])
        i += 1
    #Everything after the node we are currently at, and the current node are processed here
    i += 1
    order_starting_from_target_number.append(target_number)
    while i < len(tour):
        order_starting_from_target_number.append(tour[i])
        i += 1
    #Merges both arrays
    order_starting_from_target_number = order_starting_from_target_number + order_before_target_number
    return order_starting_from_target_number

#Finds the size of the path both tours have in common
def find_path_length(tour, compare):
    #Starts from the first node of both tours, and see how many nodes they have in common
    i = 0
    while tour[i] == compare[i] and i < len(tour) and i < len(compare):
        i += 1
    return i


def find_longest_consecutive_path(tour, tour2):
    #Removes the last node of each tour, as it is a cycle, it is not necessary
    tour.pop()
    tour2.pop()
    all_tours = []
    #Creates an array tours starting from every point
    for i in range(len(tour2)):
        all_tours.append(array_splicer(i + 1, tour2))
    #The lngest path starts out as -infinity
    longest_path = float("-inf")
    for item in tour:
        #Makes sure both tours have the same starting point
        curr_tour = array_splicer(item, tour)
        #Calculates the longest path
        longest_path = max(longest_path, find_path_length(curr_tour, all_tours[item - 1]))
    return longest_path
