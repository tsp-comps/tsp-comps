def number_of_common_edges(tour1, tour2):
    i = 0
    j = 1
    edges = set()
    while j < len(tour1):
        edges.add((tour1[i], tour1[j]))
        i += 1
        j += 1
    i = 0
    common_edges = 0
    j = 1
    while j < len(tour2):
        if (tour2[i], tour2[j]) in edges:
            common_edges += 1
        i += 1
        j += 1
    return common_edges



def array_splicer(target_number, tour):
    order_starting_from_target_number = []
    order_before_target_number = []
    i = 0
    while True:
        if tour[i] == target_number:
            break
        order_before_target_number.append(tour[i])
        i += 1

    i += 1
    order_starting_from_target_number.append(target_number)
    while i < len(tour):
        order_starting_from_target_number.append(tour[i])
        i += 1
    order_starting_from_target_number = order_starting_from_target_number + order_before_target_number
    return order_starting_from_target_number

def find_path_length(tour, compare):
    i = 0
    while tour[i] == compare[i] and i < len(tour) and i < len(compare):
        i += 1
    return i


def find_longest_consecutive_path(tour, tour2):
    tour.pop()
    tour2.pop()
    all_tours = []
    for i in range(len(tour2)):
        all_tours.append(array_splicer(i + 1, tour2))
    longest_path = float("-inf")
    for item in tour:
        curr_tour = array_splicer(item, tour)
        longest_path = max(longest_path, find_path_length(curr_tour, all_tours[item - 1]))
    return longest_path