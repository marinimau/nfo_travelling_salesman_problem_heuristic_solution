def load_costs_matrix(filename):
    costs = []
    read = False
    f = open(filename, "r")
    for line in f:
        # Skip last line
        if "];" in line:
            read = False
        # Read row, replace wrong character and convert into float list
        if read:
            row = line.replace('[', '')
            row = row.replace('],', '')
            row = row.replace(']', '')
            row = row.split(',')
            row = [float(x) for x in row]
            costs.append(row)
        # Start reading values
        if "C = [" in line:
            read = True

    return costs
