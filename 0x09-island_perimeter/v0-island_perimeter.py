#!/usr/bin/python3
"""Module defines the island_perimeter(grid) function"""

from typing import List


Dict = {'matches': 0,
        'prev_index_list': [],
        'prev_contribution': 0,
        'perimeter': 0}

def list_contribution(Mlist: List):
    cont = Dict['prev_contribution'] - Dict['matches']
    print(cont)
    Dict['perimeter'] = Dict['perimeter'] + cont
    value = 4 + 2*(len(Mlist) - 1)
    Dict['prev_contribution'] = value


def index_comparison(Plist: List):
    for v in Dict['prev_index_list']:
        for k in Plist:
            if k == v:
                Dict['matches'] = Dict['matches'] + 1


def index_list(Clist: List):
    indx_list = []
    indx = 0
    for v in Clist:
        if v == 1:
            indx_list.append(indx)
        indx = indx + 1
    print(indx_list)
    index_comparison(indx_list)
    list_contribution(indx_list)

def island_perimeter(grid):
    for i in range(1, len(grid)):
        index_list(grid[i])
#        print(Dict['perimeter'])
    return Dict['perimeter']
