'''
The basic idea is to maintain another boolean matrix ‘isZero’ which stores whether our resultant matrix should contain a zero at a 
particular index or not. We can traverse every element of our original matrix. If the element is 0, then we traverse the complete 
row and complete column of that particular element and set isZero values accordingly to true for all the elements in that row and 
column.

Time Complexity : We are traversing each element. For each element that is zero, we are traversing its complete row and column. So 
we have O(M * N) elements and for each element, we can traverse a row and a column in the worst case, i.e. O(M + N). So total complexity 
is O(M * N * (M + N).

Space Complexity : We need to declare a 2D boolean matrix of size n x m. So the total required space will be O(N * M).

'''
from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:

    # Storing dimensions of matrix in n and m.
    n = len(matrix)
    m = len(matrix[0])
	
    # Declaring isZero boolean matrix.
    isZero = [[False for _ in range(m)] for _ in range(n)]
	
	# Traversing the original matrix.
    for i in range(n):
        for j in range(m):
			
			# If that element of the matrix is equal to 0.
            if matrix[i][j] == 0:
				
				# Traversing its complete column and setting all the isZero values to be true.
                for k in range(n):
                    isZero[k][j] = True
				
				# Traversing its complete row and setting all the isZero values to be true.
                for k in range(m):
                    isZero[i][k] = True
	
	# Travrsing isZero and if isZero at an index is true then we replace that element with zero in original matrix.
    for i in range(n):
        for j in range(m):
            if isZero[i][j]:
                matrix[i][j] = 0
    pass