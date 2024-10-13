"""
https://leetcode.com/problems/surrounded-regions/description/



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

            if 0<= nrow < m and 0<= ncol < n and visited_array[nrow][ncol]==0 and mat[nrow][ncol]=="O":
                visited_array[nrow][ncol]=1
                self.dfs(nrow, ncol, visited_array, mat)
               
        return mat, visited_array


    def bfs(self, row, col, visited_array, mat):
        m=len(mat)
        n=len(mat[0])
        q = deque()

        q.append((row, col))

        while q:
            size = len(q)
            while size > 0:
                size-=1
                (row, col) = q.popleft()

                dx = [-1, 0, 0, 1]
                dy = [0, -1, 1, 0]

                for r in range(4):
                    nrow = row + dx[r]
                    ncol = col + dy[r]
                    if 0<= nrow < m and 0<= ncol < n and visited_array[nrow][ncol]==0 and mat[nrow][ncol]=="O":
                        q.append((nrow, ncol))
                        visited_array[nrow][ncol]=1
        return mat, visited_array





    def dfs_driver(self, mat):
        m=len(mat)
        n=len(mat[0])

        visited_array = [[0 for i in range(n)] for j in range(m)]

        #first col
        for i in range(m):
            if mat[i][0] == "O":
                visited_array[i][0] = 1
                # self.dfs(i, 0, visited_array, mat)
                self.bfs(i, 0, visited_array, mat)
        
        #first row
        for j in range(n):
            if mat[0][j]=="O":
                visited_array[0][j] = 1
                # self.dfs(0, j, visited_array, mat)
                self.bfs(0, j, visited_array, mat)

        #last col
        for i in range(m):
            if mat[i][n-1] == "O":
                visited_array[i][n-1] = 1
                # self.dfs(i, (n-1), visited_array, mat)
                self.bfs(i, (n-1), visited_array, mat)

        #last row
        for j in range(n):
            if mat[m-1][j]=="O":
                visited_array[m-1][j] = 1
                # self.dfs(m-1, j, visited_array, mat)
                self.bfs(m-1, j, visited_array, mat)


        for i in range(m):
            for j in range(n):
                if mat[i][j] == "O" and visited_array[i][j]==0:
                    mat[i][j]="X"    

        return mat


sol = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

print(sol.dfs_driver(board))