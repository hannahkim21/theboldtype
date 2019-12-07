import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import networkx as nx

from student_utils import *
"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_locations: A list of locations such that node i of the graph corresponds to name at index i of the list
        list_of_homes: A list of homes
        starting_car_location: The name of the starting location for the car
        adjacency_matrix: The adjacency matrix from the input file
    Output:
        A list of locations representing the car path
        A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
        NOTE: both outputs should be in terms of indices not the names of the locations themselves
    """
    #0.0 Convert the names into indices
    start_ind = list_of_locations.index(starting_car_location)
    index_locs = convert_locations_to_indices(list_of_locations, list_of_locations)
    index_locs.remove(start_ind)
    index_homes = convert_locations_to_indices(list_of_homes, list_of_locations)
    index_homes.remove(start_ind)

    #0.1 Create the graph object
    G = adjacency_matrix_to_graph(adjacency_matrix)[0]

    #1 Degree list of tuples
    degrees = []
    for i in range(len(list_of_locations)):
        tup = (i, G.degree(i))
        degrees.append(tup)

    #2 Sort by degree
    degrees = sorted(degrees, key = lambda x: -x[1])

    #Cluster representation
    cluster_dict = {}

    #3 Iterate through cluster_count
    home_count = len(index_homes)
    for i in range(home_count):
        # Find the node of maximal degree
        max_node = degrees[0][0]
        cluster_dict[max_node] = []

        # Determine the cutoff distance to be added
        neighbor_list = [n for n in G.neighbors(max_node)]
        distance_total_sum = 0
        for n in neighbor_list:
            distance_total_sum += nx.shortest_path_length(G, max_node, n, weight=None)

        cutoff = distance_total_sum / len(neighbor_list)

        # Add home nodes within cutoff distance to max degree's cluster
        for node in neighbor_list:
            if node in index_homes:
                if nx.shortest_path_length(G, max_node, node, weight=None) <= cutoff:
                    cluster_dict[max_node].append([node])
                    # Remove nodes added from index_homes, index_locs
                    index_homes.remove(node)
                    index_locs.remove(node)

        # Remove node of maximal degree from index_locs
        index_locs.remove(max_node)
        degrees.pop(0)

        #Check cutoff
        k = 0
        for h in cluster_dict.values():
            k += len(h)
            if k / len(list_of_homes) > .7:
                break
        else:
            continue

        break

    # Add leftover nodes to existing clusters
    if (len(index_homes) != 0):
        minlen = 2500000000
        closest = None
        list_of_cluster = cluster_dict.keys()
        for node in index_homes:
            for clust in list_of_cluster:
                if nx.shortest_path_length(G, node, clust, weight=None) < minlen:
                    minlen = nx.shortest_path_length(G, node, clust, weight=None)
                    closest = clust
            cluster_dict[closest].append([node])

    #4 Find the shortest path between the clusters
    path = []
    path.append(start_ind)

    # Path from start to first cluster
    minlen = 2500000000
    first = None
    for cluster in cluster_dict.items():
        node = cluster[0]
        if nx.shortest_path_length(G, start_ind, node, weight=None) < minlen:
            minlen = nx.shortest_path_length(G, start_ind, node, weight=None)
            first = node
    path.append(first)

    # Path between clusters
    tempcluster = cluster_dict.keys()
    minlen = 2500000000
    curr = first
    while tempcluster != None:
        for cluster in cluster_dict.items():
            node = cluster[0]
            if nx.shortest_path_length(G, start_ind, node, weight=None) < minlen:
                minlen = nx.shortest_path_length(G, start_ind, node, weight=None)
                curr = node
        path.append(curr)

    last = curr
    # Path back to start
    path.append(nx.shortest_path_length(G, last, start_ind, weight=None))

    return path, cluster_dict

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

"""
Convert solution with path and dropoff_mapping in terms of indices
and write solution output in terms of names to path_to_file + file_number + '.out'
"""
def convertToFile(path, dropoff_mapping, path_to_file, list_locs):
    string = ''
    for node in path:
        string += list_locs[node] + ' '
    string = string.strip()
    string += '\n'

    dropoffNumber = len(dropoff_mapping.keys())
    string += str(dropoffNumber) + '\n'
    for dropoff in dropoff_mapping.keys():
        strDrop = list_locs[dropoff] + ' '
        for node in dropoff_mapping[dropoff]:
            strDrop += list_locs[node] + ' '
        strDrop = strDrop.strip()
        strDrop += '\n'
        string += strDrop
    utils.write_to_file(path_to_file, string)

def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)

    input_data = utils.read_file(input_file)
    num_of_locations, num_houses, list_locations, list_houses, starting_car_location, adjacency_matrix = data_parser(input_data)
    car_path, drop_offs = solve(list_locations, list_houses, starting_car_location, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_file = utils.input_to_output(input_file, output_directory)

    convertToFile(car_path, drop_offs, output_file, list_locations)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)
