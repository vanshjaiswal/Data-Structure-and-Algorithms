"""
Prims algorithm is used for finding the sum of Minimum spanning tree and you can get 
the minimum spanning tree as well.

This is used for weighted undirected connected graph


"""

import heapq
class Graph:
    def prims_algorithm(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for src, des, wt in edges:
            adj_list[src].append([des, wt])
            adj_list[des].append([src, wt])

        visited_arr = [0 for i in range(n)]
        MST = []
        mst_sum = 0
        
        #heapq will contain(weight, node, parent)

        q = [(0, 0, -1)]
        while q:
            weight, node, parent = heapq.heappop(q)
            if visited_arr[node] != 1:
                visited_arr[node] = 1
                mst_sum += weight
                if parent != -1:
                    MST.append((node, parent))

            neighbours = adj_list[node]
            for cur_node, wt in neighbours:
                if visited_arr[cur_node] != 1:
                    heapq.heappush(q, (wt, cur_node, node))

        return mst_sum, MST

V = 5
edges = [ [0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]] 
sol = Graph()
print(sol.prims_algorithm(V, edges))
                


