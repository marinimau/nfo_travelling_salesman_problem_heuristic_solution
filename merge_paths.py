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

from operator import itemgetter


def compute_cost_karp_steele(t1, t2, costs):
    """
    Compute the cost following the karp-steele formula (the sum of the cost of the two new arcs minus the sum of the
    two old arcs). Given t1 = (A, B) and t2 = (C, D), with A and C the starting point of the old arcs and C and D the
    ending point of the old arcs, the new arc are composed by the tuples (A, D) and (C, B).
    :param t1: A tuple with the first arc to remove
    :param t2: A tuple with the second arc to remove
    :param costs: The matrix cost
    :return: Float with the cost of the change of the arcs
    """
    return costs[t1[0]][t2[1]] + costs[t2[0]][t1[1]] - (costs[t1[0]][t1[1]] - costs[t2[0]][t2[1]])


def get_biggest_sub_path(paths):
    """
    Return the biggest paths
    :param paths: the (path, node_counter) list
    :return: the biggest path
    """
    biggest = max(paths, key=itemgetter(1))
    paths.remove(biggest)
    return biggest


def split_path(path, val):
    """
    Split the path when it encounter a certain value
    :param path: the path list
    :param val: the value
    :return: two sub paths -> sub_path1 from start to value / sub_path2 form after the value to the end
    """
    sub_path1 = []
    sub_path2 = path[:-1]
    for i in path:
        sub_path1.append(i)
        sub_path2.remove(i)
        if i == val:
            break
    return sub_path1, sub_path2


def get_cost_for_each_couple_of_arcs(path1, path2, costs):
    """
    Get the cost of the karp and steele formula for each couple of arcs
    :param path1: List with all the nodes of the first path
    :param path2: List with all the nodes of the second path
    :param costs: Cost matrix
    :return: A list of tuples (cost, (starting node of the first arc, starting node of the second arc))
    """
    result = []
    for i in range(len(path1) - 1):
        for j in range(len(path2) - 1):
            result.append((compute_cost_karp_steele((path1[i], path1[i + 1]), (path2[j], path2[j + 1]), costs),
                           (path1[i], path2[j])))
    return result


def get_new_path(path1, path2, start):
    """
    Get the new path deleting two old arcs and inserting the two new arcs
    :param path1: List with all the nodes of the first path
    :param path2: List with all the nodes of the second path
    :param start: A tuple with the splitting node of the first path and the splitting node of the second path
    :return: The new path with the old arcs removed and the new ones inserted
    """
    sp1, sp2 = split_path(path1, start[0])
    sp3, sp4 = split_path(path2, start[1])
    sp2.append(sp1[0])
    new_path = sp1 + sp4 + sp3 + sp2
    return new_path


def merge_sub_paths(paths, costs):
    """
    Merge the sub paths
    :param costs:
    :param paths: the (path, node_counter) list
    :return:
    """
    # Get the two biggest sub paths
    sub_path1 = get_biggest_sub_path(paths)
    sub_path2 = get_biggest_sub_path(paths)

    # Get the karp steele cost for each couple of arcs
    result = get_cost_for_each_couple_of_arcs(sub_path1[0], sub_path2[0], costs)
    # Get the couple of arcs with the minimum cost
    min_cost = min(result, key=itemgetter(0))
    # Get the new path create with the deletion and addition of two arcs
    new_path = get_new_path(sub_path1[0], sub_path2[0], min_cost[1])
    # Add the new path to the list of sub paths
    paths.append((new_path, sub_path1[1] + sub_path2[1]))
