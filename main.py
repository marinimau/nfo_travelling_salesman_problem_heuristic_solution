from create_model import *
from load_dataset import *

# Costs Matrix
costs = []

# Number of nodes
nodes = len(costs)
# Range of the nodes
range_nodes = range(nodes)

if __name__ == '__main__':
    costs = load_costs_matrix("dataset/br17.dat")
    # Number of nodes
    nodes = len(costs)
    # Range of the nodes
    range_nodes = range(nodes)

    # Create the model
    m = create_assignment_model('tsp_heuristic', range_nodes, costs)
    m.print_information()
    solution = m.solve()
    m.report()
    print(solution)
