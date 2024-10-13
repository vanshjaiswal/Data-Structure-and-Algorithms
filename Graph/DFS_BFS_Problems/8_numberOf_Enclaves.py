"""
https://leetcode.com/problems/number-of-enclaves/description/


You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


Input: grid =

[[0,0,0,0],
[1,0,1,0],
[0,1,1,0],
[0,0,0,0]]

Output: 3

"""
from collections import deque
class Solution:
    def dfs(self, row, col, visited_array, mat):
        m=len(mat)
        n=len(mat[0])

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        for r in range(4):
            nrow = row + dx[r]
            ncol = col + dy[r]

            if 0<=nrow< m and 0<=ncol< n and visited_array[nrow][ncol] == 0 and mat[nrow][ncol]==1:
                visited_array[nrow][ncol] = 1
                self.dfs(nrow, ncol, visited_array, mat)

        return mat, visited_array


    def bfs(self, row, col, visited_array, mat):
        m=len(mat)
        n=len(mat[0])

        q= deque()
        q.append((row, col))

        while q:
            size = len(q)
            while size > 0:
                size -= 1
                (row, col) = q.popleft()
                dx = [-1, 0, 0, 1]
                dy = [0, -1, 1, 0]

                for r in range(4):
                    nrow = row + dx[r]
                    ncol = col + dy[r]
                    if 0<=nrow< m and 0<=ncol< n and visited_array[nrow][ncol] == 0 and mat[nrow][ncol]==1:
                        visited_array[nrow][ncol] = 1
                        q.append((nrow, ncol))

        return mat, visited_array



    def numEnclaves(self, mat):
        m=len(mat)
        n=len(mat[0])

        visited_array = [[0 for i in range(n)] for j in range(m)]

        #first col
        for i in range(m):
            if mat[i][0] == 1:
                visited_array[i][0] = 1
                # self.dfs(i, 0, visited_array, mat)
                self.bfs(i, 0, visited_array, mat)
        
        #first row
        for j in range(n):
            if mat[0][j]==1:
                visited_array[0][j] = 1
                # self.dfs(0, j, visited_array, mat)
                self.bfs(0, j, visited_array, mat)

        #last col
        for i in range(m):
            if mat[i][n-1] == 1:
                visited_array[i][n-1] = 1
                # self.dfs(i, (n-1), visited_array, mat)
                self.bfs(i, (n-1), visited_array, mat)

        #last row
        for j in range(n):
            if mat[m-1][j]==1:
                visited_array[m-1][j] = 1
                # self.dfs(m-1, j, visited_array, mat)
                self.bfs(m-1, j, visited_array, mat)
        count = 0
        print(visited_array)
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and visited_array[i][j] == 0 :
                    count += 1

        return count
            

sol = Solution()

grid = [[0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0]]

print(sol.numEnclaves(grid))