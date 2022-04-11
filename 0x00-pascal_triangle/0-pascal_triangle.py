#!/usr/bin/python3
""" Pascal's Triangle """
from typing import List

def pascal_triangle(n: int) -> List:
    """
    Pascal's Triangle 
    
    Args:
        n (int): triangle's deep

    Returns:
        List: Pascal's Triangle List
    """
    l = []
    if n <= 0:
        return l
    l.append([1])
    for i in range(1, n):
        tmp = [1]
        for j in range(len(l[i - 1]) - 1):
            current = l[i - 1]
            tmp.append(l[i - 1][j] + l[i - 1][j + 1])
        tmp.append(1)
        l.append(tmp)
    return l
        