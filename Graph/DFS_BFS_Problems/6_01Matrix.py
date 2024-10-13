"""
https://leetcode.com/problems/01-matrix/


Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


we can use BFS as we have to find the distance step wise
"""

from collections import deque
class Solution:
    def updateMatrix(self, mat):
        m=len(mat)
        n=len(mat[0])

        visited_array = [[0 for i in range(n)] for j in range(m)]
        distance_matrix = [[0 for i in range(n)] for j in range(m)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    q.append(((i,j), 0))
                    visited_array[i][j] = 1
                    distance_matrix[i][j] = 0

        
        while q:
            (i,j), distance = q.popleft()

            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]

            for r in range(4):
                row = i + dx[r]
                col = j + dy[r]

                if 0<=row<m and 0<=col<n and mat[row][col] == 0 and visited_array[row][col]==0:
                    q.append(((row, col), distance+1))
                    visited_array[row][col] = 1
                    distance_matrix[row][col] = distance + 1

        return distance_matrix



sol = Solution()
mat = [[0,0,0],
[0,1,0],
[1,0,1]]

mat = [[0,0,0],[0,1,0],[0,0,0]]

print(sol.updateMatrix(mat))
                

# [[0, 2, 0], 
# [0, 1, 2], 
# [1, 0, 1]]