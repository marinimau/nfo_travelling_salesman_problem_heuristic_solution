from docplex.mp.model import Model


def create_assignment_model(name, range_nodes, costs):
    m = Model(name=name, log_output=True)

    # Decision Variable
    x = m.binary_var_matrix(range_nodes, range_nodes)

    # In-degree and Out-degree of each vertex
    for i in range_nodes:
        m.add_constraint(m.sum(x[i, j] for j in range_nodes) == 1)
    for j in range_nodes:
        m.add_constraint(m.sum(x[i, j] for i in range_nodes) == 1)

    # No loop from the same node
    for i in range_nodes:
        for j in range_nodes:
            if i == j:
                m.add_constraint(x[i, j] == 0)

    # Objective Function
    m.minimize(m.sum(costs[i][j] * x[i, j] for j in range_nodes for i in range_nodes))

    return m
