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

from docplex.mp.model import Model


def create_assignment_model(name, range_nodes, costs):
    """
    Create assignment model
    :param name: the name of the model
    :param range_nodes: the range nodes
    :param costs: the cost
    :return:
    """
    m = Model(name=name, log_output=True)
    # Decision Variable
    x = m.binary_var_matrix(range_nodes, range_nodes)
    # In-degree and Out-degree of each vertex
    [m.add_constraint(m.sum(x[i, j] for j in range_nodes) == 1) for i in range_nodes]
    [m.add_constraint(m.sum(x[i, j] for i in range_nodes) == 1) for j in range_nodes]
    # No loop from the same node
    [m.add_constraint(x[i, i] == 0) for i in range_nodes]
    # Objective Function
    m.minimize(m.sum(costs[i][j] * x[i, j] for j in range_nodes for i in range_nodes))
    return m
