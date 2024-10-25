"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/


Input: grid = [[0,0,0],
                [1,1,0],
                [1,1,0]]
Output: 4

src = 0,0
dest = n-1, n-1

"""

from collections import deque
class Graph:
    def shortest_path(self, grid):
        n=len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        dist = [[float("inf") for _ in range(n)] for __ in range(n)]


        dist[0][0] = 0

        q = deque()
        q.append((0, (0,0)))
        dx = [-1, 0, 0, 1, -1, -1, 1, 1]
        dy = [0, -1, 1, 0, -1, 1, -1, 1]

        while q:
            distance, (row, col) = q.popleft()

            for r in range(8):
                nrow = row + dx[r]
                ncol = col + dy[r]
                
                if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == 0 and dist[nrow][ncol] > dist[row][col]+1:
                    dist[nrow][ncol] = dist[row][col]+1
                    q.append((dist[row][col]+1, (nrow, ncol)))

        if dist[n-1][n-1] != float("inf"):
            return dist[n-1][n-1] + 1
        return -1


sol=Graph()


grid = [[0,0,0],
                [1,1,0],
                [1,1,0]]

print(sol.shortest_path(grid))


