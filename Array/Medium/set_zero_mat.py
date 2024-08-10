"""

https://takeuforward.org/data-structure/set-matrix-zero/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
https://takeuforward.org/data-structure/set-matrix-zero/
"""
def mark_row(matrix, n,m,i):
    for j in range(m):
        if matrix[i][j]!=0:
            matrix[i][j] = -1
    

def mark_col(matrix, n,m,j):
    for i in range(n):
        if matrix[i][j]==1:
            matrix[i][j] = -1
    

def set_zero(matrix, n, m):
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                mark_row(matrix, n,m,i)
                mark_col(matrix,n,m, j)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    return matrix
    

# print(set_zero([[1,1,1],[1,0,1],[1,1,1]], 3, 3))
# print(zeroMatrix([[1,1,1],[1,0,1],[1,1,1]], 3, 3))


#Better Approach


def set_zero_better(matrix):
    n=len(matrix)
    m=len(matrix[0])

    col_list = [0]*m
    row_list = [0]*n

    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row_list[i]=1
                col_list[j]=1
            
    for i in range(n):
        for j in range(m):
            if row_list[i] ==1 or col_list[j] == 1:
                matrix[i][j]=0
    return matrix

print(set_zero_better([[1,1,1],[1,0,1],[1,1,1]]))


#Optimal

