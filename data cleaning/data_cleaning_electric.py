import math
from haversine import *

#We calculate the distance between the two points, and output the distance in Miles
def distance(point1, point2):
    distance = haversine(point1, point2, unit = "mi")
    return distance

#We will read the dataset and add every point of it to a set.
#This way we ensure we have all points of the graph and no duplicates
file = open("datasets/electric-grid/costs.txt", "r")
coordinate_spots = set()
for line in file:
    split_line = line.split("\t")[4:8]
    if split_line[0] != '' and split_line[1] != '':
        coordinate_spots.add((float(split_line[0]), float(split_line[1])))
    if split_line[2] != '' and split_line[3] != '':
        coordinate_spots.add((float(split_line[2]), float(split_line[3])))
file.close()
    

#Here we calculate the distance between every pair of nodes, and add them to an output file
#The format of the output file is coordinates of point a, coordinates of point b, distance from a to b
output_file = open("datasets/electric-grid/electric_points.tsv", "w")
for item in coordinate_spots:
    for item2 in coordinate_spots:
        if item != item2 and item != ("", "") and item2 != ("", ""):
            distance_points = distance(item, item2)
            output_file.write(str(item)+"\t"+str(item2)+"\t"+str(distance_points)+"\n")
output_file.close()    
