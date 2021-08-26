import numpy


def convert_row(d, nodes):
    row = int(int(d['name'][1:]) / nodes) + 1
    col = int(int(d['name'][1:]) % nodes)
    if col == 0:
        col = nodes
        row = row - 1
    return row, col


def convert_dataframe_names(df, nodes):
    start = []
    end = []
    for index, d in df.iterrows():
        pos = convert_row(d, nodes)
        start.append(pos[0] - 1)
        end.append(pos[1] - 1)
    df.drop('name', axis=1, inplace=True)
    df['start'] = start
    df['end'] = end
    return df


# Get the decision variable x in matrix form
# Args:
#   df (pd.dataframe) -> the dataframe with the solution of the model
#   nodes (int) -> the number of the nodes
# Returns:
#   (ndarray) -> The matrix
def solution_to_matrix(df, nodes):
    matrix = numpy.zeros((nodes, nodes))
    for index, d in df.iterrows():
        pos = convert_row(d, nodes)
        row = pos[0] - 1
        col = pos[1] - 1
        matrix[row][col] = 1
    return matrix

