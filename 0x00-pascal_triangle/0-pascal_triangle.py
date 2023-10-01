#!/usr/bin/python3
""" module with a Function that implements Pascal's triangle """


def pascal_triangle(n):
    """Pascal's triangle Functon"""

    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    # print(triangle)
    return triangle
