#!/usr/bin/python3
"""module defines island_perimeter(grid)"""


def check(x):
    """function checks if x is 0 or 1
    """

    if x == 0:
        return 1
    return 0


def island_perimeter(grid):
    """function returns the perimeter of the island described
       in grid(grid is a list of list of integers);
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        - grid is rectangular, with its width and height not exceeding 100
    """

    row = len(grid)
    col = len(grid[0])

    assert 1 <= row <= 100, "length must be between 1 and 100"
    assert 1 <= col <= 100, "height must be between 1 and 100"

    perim = 0
    for i in range(row):
        for j in range(col):
            assert grid[i][j] == 0 or grid[i][j] == 1,\
                                     "grid must have only 1 or 0 values"

            if grid[i][j] == 1:
                if i - 1 < 0:
                    perim += 1
                else:
                    perim += check(grid[i - 1][j])
                if j - 1 < 0:
                    perim += 1
                else:
                    perim += check(grid[i][j - 1])
                try:
                    perim += check(grid[i + 1][j])
                except IndexError:
                    perim += 1
                try:
                    perim += check(grid[i][j + 1])
                except IndexError:
                    perim += 1
    return perim
