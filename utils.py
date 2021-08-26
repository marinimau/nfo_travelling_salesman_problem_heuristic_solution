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

import numpy


def convert_row(d, nodes):
    """
    Convert row
    :param d:
    :param nodes:
    :return:
    """
    row = int(int(d['name'][1:]) / nodes) + 1
    col = int(int(d['name'][1:]) % nodes)
    if col == 0:
        col = nodes
        row = row - 1
    return row, col


def convert_dataframe_names(df, nodes):
    """
    Convert dataframe names
    :param df:
    :param nodes:
    :return:
    """
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


def solution_to_matrix(df, nodes):
    """
    Get the decision variable x in matrix form
    :param df: a Pandas dataframe that contains the solution of the model
    :param nodes: the number of nodes
    :return: the matrix that contains the solution
    """
    matrix = numpy.zeros((nodes, nodes))
    for index, d in df.iterrows():
        pos = convert_row(d, nodes)
        row = pos[0] - 1
        col = pos[1] - 1
        matrix[row][col] = 1
    return matrix
