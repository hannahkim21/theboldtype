import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils import *
import input_validator

def objectiveFn(input_file, output_file, params=[]):
	number_of_locations, number_of_houses, list_of_locations, list_of_houses, starting_location, adjacency_matrix = data_parser(input_data)
	try:
        G, message = adjacency_matrix_to_graph(adjacency_matrix)
    except Exception:
        return 'Your adjacency matrix is not well formed.\n', 'infinite'
	return -cost_cost_of_solution(G, car_cycle, dropoff_mapping)