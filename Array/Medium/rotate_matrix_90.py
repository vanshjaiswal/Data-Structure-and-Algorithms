"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
https://leetcode.com/problems/rotate-image/description/

https://takeuforward.org/data-structure/rotate-image-by-90-degree/

"""

def rotate_matrix(matrix):
    n = len(matrix)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated

# print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))

#Optimal

"""
Intuition: By observation, we see that the first column of the original matrix is the reverse of the first row of the rotated matrix, so that’s why we transpose the matrix and then reverse each row, and since we are making changes in the matrix itself space complexity gets reduced to O(1).

Approach:

"""

def rotate_matrix2(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
    
    return matrix

print(rotate_matrix2([[1,2,3],[4,5,6],[7,8,9]]))


