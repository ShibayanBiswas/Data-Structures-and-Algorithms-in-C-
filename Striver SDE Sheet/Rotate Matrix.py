'''

We will consider the given matrix in the form of rings/squares, and this time, we will rotate the matrix in an iterative manner. 
1. Initialise two variables, ‘row’ and ‘col’ to keep track of the starting row and starting column of the current ring. Ending row 
    and ending column can be tracked by N and M.
2. Starting from the outer ring, keep rotating the inner rings, if it exists.
3. For each ring/square of the matrix: Move the elements of the top side. Move the elements of the right side. Move the elements of
   the bottom side. Move the elements of the left side. Update the ‘row’, ‘col’, ‘N’ and ‘M’ for the next inner ring.

Time Complexity : O(N * M), where N is the number of rows and M is the number of columns in the matrix. Since we are traversing each
element of the matrix just once, the time complexity of the above algorithm is O(N * M). 

Space Complexity : O(1). We are not using any extra data structure, as we are updating the given matrix. Only constant extra space 
is required. Thus, the space complexity is O(1).

'''

def rotateMatrix(mat, n, m):
    row = 0
    col = 0

    ''' 
       row - Staring row index 
       m - ending row index 
       col - starting column index 
       n - ending column index  
    '''
    
    while (row < n and col < m):
        # If we have rotated the whole matrix
        if (row == n - 1 or col == m - 1):
            break
        # Store the first element of next row as this element will replace first element of current row
        previous = mat[row + 1][col]
        # Move elements of first row from the remaining rows
        for i in range(col, m):
            current = mat[row][i]
            mat[row][i] = previous
            previous = current
        row += 1
        # Move elements of last column from the remaining columns
        for i in range(row, n):
            current = mat[i][m-1]
            mat[i][m-1] = previous
            previous = current
        m -= 1
        # Move elements of last row from the remaining rows
        if (row < n):
            for i in range(m-1, col-1, -1):
                current = mat[n-1][i]
                mat[n-1][i] = previous
                previous = current
        n -= 1
        # Move elements of first column from the remaining rows
        if (col < m):
            for i in range(n-1, row-1, -1):
                current = mat[i][col]
                mat[i][col] = previous
                previous = current
        col += 1
