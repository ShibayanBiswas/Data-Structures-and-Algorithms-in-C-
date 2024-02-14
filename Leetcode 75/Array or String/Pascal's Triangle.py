'''

The idea is to use the definition of pascal’s triangle that its coefficients and are summation of adjacent elements in preceding rows.
so in this way we can store the elements in a matrix and for further generation of values in it we can check the preceding elements 
and update the value.

Time Complexity : O(N^2), Where ‘N’ denotes the number of Rows. We are using two nested loops.

Space Complexity : O(N^2),  Where ‘N’ denotes the number of Rows. We are using an ArrayList of ArrayList to store values.

'''

def printPascal(n):
    triangle = []
    for row in range(n):
        add = []
        for i in range(row+1):
            if row == i or i == 0:
                add.append(1)
            else:
                add.append(triangle[row - 1][i - 1] + triangle[row - 1][i])
        triangle.append(add)
    return triangle