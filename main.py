"""
Copyright (c) 2021 Mauro Marini, Andrea Piras

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

from create_model import *
from load_dataset import *
from utils import *
from subpath_finder import *


# Costs Matrix
costs = []

if __name__ == '__main__':
    costs = load_costs_matrix("dataset/br17.dat")
    # Number of nodes
    nodes = len(costs)
    # Range of the nodes
    range_nodes = range(nodes)
    # Create the model
    m = create_assignment_model('tsp_heuristic', range_nodes, costs)
    # m.print_information()
    solution = m.solve()
    # m.report()
    # print(solution)
    df = solution.as_df()
    df = convert_dataframe_names(df, nodes)
    paths = get_paths(df, nodes)
    print(paths)
