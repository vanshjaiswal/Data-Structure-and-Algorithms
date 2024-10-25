"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

Based on floyd warshall

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
AT MOST distanceThresold
"""

class Graph:
    def findTheCity(self, n, edges, distanceThreshold):
        adj_mat = [[float("inf") for i in range(n)] for j in range(n)]
        for src, des, wt in edges:
            adj_mat[src][des] = wt
            adj_mat[des][src] = wt
        
        for i in range(n):
            adj_mat[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k] + adj_mat[k][j])
        
        dic = dict(zip(list(range(n)), [0]*n))
        for i in range(n):
            for j in range(n):
                if adj_mat[i][j] <= distanceThreshold and i!=j:
                    dic[i] += 1

        val = min(list(dic.values()))

        mx = float("-inf")
        for i in dic.keys():
            if dic[i] == val:
                mx = max(mx, i)

        return mx


sol = Graph()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
# n = 5
# edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
# distanceThreshold = 2
print(sol.findTheCity(n, edges, distanceThreshold))

[[0, 3, 4, 5], 
[3, 0, 1, 2], 
[4, 1, 0, 1], 
[5, 2, 1, 0]]



[[4, 2, 5, 5, 4], 
[2, 4, 3, 3, 2], 
[5, 3, 2, 1, 2], 
[5, 3, 1, 2, 1], 
[4, 2, 2, 1, 2]]