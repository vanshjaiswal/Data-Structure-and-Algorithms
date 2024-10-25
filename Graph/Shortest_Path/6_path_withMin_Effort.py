"""
https://leetcode.com/problems/path-with-minimum-effort/description/

Input: heights = [[1,2,2],
                [3,8,2],
                [5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

"""

import heapq
class Graph:
    def minPath_Effort(self, heights):
        m=len(heights)
        n=len(heights[0])
        dist = [[float("inf") for _ in range(m)] for j in range(n)]

        dist[0][0] = 0

        q = heapq.heappush((0, (0,0)))
        dist[0][0] = 0

        while q:
            effort, (row, col) = heapq.heappop(q)
            if row == m-1 and col ==n-1:
                return effort
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 0, 1]
            for i in range(4):
                nrow = row + dx[i]
                ncol = col + dy[i]

                if 0<= nrow < m and 0<=ncol<n:
                    newEffort = max(abs(heights[row][col] - heights[nrow][ncol]), effort)
                    if newEffort < dist[nrow][ncol]:
                        dist[nrow][ncol] = newEffort
                        heapq.heappush(q, (newEffort, (nrow, ncol)))
        return 0
        