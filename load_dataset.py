def load_costs_matrix(filename):
    costs = []
    read = False
    f = open(filename, "r")
    for line in f:
        if "];" in line:
            read = False
        if read:
            row = line.replace('[', '')
            row = row.replace('],', '')
            row = row.replace(']', '')
            row = row.split(',')
            row = [float(x) for x in row]
            costs.append(row)
        if "C = [" in line:
            read = True

    return costs
