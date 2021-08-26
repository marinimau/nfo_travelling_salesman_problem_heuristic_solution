# Get the next non visited node
# Args:
#   visited (boolean list) -> List that track which nodes have been visited
# Returns:
#   (int) -> -1 if all nodes have been visited or the index of the first node that hasn't been visited
def get_next_node(visited):
    for idx, val in enumerate(visited):
        if not val:
            return idx
    return -1


# Return all the sub paths
# Args:
#   df (pd.dataframe) -> the dataframe with the solution of the model
#   nodes (int) -> the number of the nodes
# Returns:
#   (list of list) -> the list of sub paths
def get_paths(df, nodes):
    visited = [False] * nodes
    paths = []
    path = []
    # Set the node 1 to visited and add it to the path
    visited[df['start'].iloc[0]] = True
    path.append(df['start'].iloc[0] + 1)
    # Take the endpoint of the arc
    next = df['end'].iloc[0]
    while next != -1:
        # Set the start node to the visited and add it to the path
        visited[df['start'].iloc[next]] = True
        path.append(df['start'].iloc[next] + 1)
        # If the end of the arc is not visited
        if not visited[df['end'].iloc[next]]:
            # Change the next node with the end of the arc
            next = df['end'].iloc[next]
        # If the end of the arc is visited
        else:
            # Add the end node to the path
            path.append(df['end'].iloc[next] + 1)
            # Add the sub path to the paths list
            paths.append(path)
            # Start a new path
            path = []
            # Get the next node not visited
            next = get_next_node(visited)
    return paths
