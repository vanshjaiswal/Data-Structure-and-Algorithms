"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700

We can use dijskstra. store (k, (node, cost)) in the queue intially k= -1, amount = 0, node = src
"""
from collections import deque
import heapq
class Graph:

    def adjacency_list(self, flights, n):
        adj_list = [[] for _ in range(n)]
        for src, des, wt in flights:
            adj_list[src].append([des, wt])

        return adj_list
        

    def cheapest_flight(self, n, flights, src, dst, k):
        adj_list = self.adjacency_list(flights, n)
        q = deque()
        q.append((0, (src, 0)))
        
        cost_array = [float("inf") for _ in range(n)]
        cost_array[src] = 0

        while q:
            stops, (node, cost) = q.popleft()
            if stops > k:
                continue
            neighbours = adj_list[node]
            for cur_node, wt in neighbours:
                if cost + wt < cost_array[cur_node] and stops <= k:
                    cost_array[cur_node] = cost + wt
                    q.append((stops+1, (cur_node, cost + wt)))
            
        if cost_array[dst] == float("inf"):
            return -1
        return cost_array[dst]


  


n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1

sol = Graph()
print(sol.cheapest_flight(n, flights,src,dst,k))