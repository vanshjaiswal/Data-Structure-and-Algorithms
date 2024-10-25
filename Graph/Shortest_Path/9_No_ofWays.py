"""
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/




"""

from collections import deque
import heapq
class Graph:
    def countPaths(self, n , roads):
        # adj_list = [[] for i in range(n)]
        # for src, des, wt in roads:
        #     adj_list[src].append([des, wt])
        #     adj_list[des].append([src, wt])

        # dist = [float("inf") for i in range(n)]
        # path = [0 for i in range(n)]

        # dist[0] = 0

        # q = [(0, 0)]

        # while q:
        #     distance, node = heapq.heappop(q)
        #     if node == n-1:
        #         print(node, dist, path)
        #         if distance == dist[n-1]:
        #             path[n-1] += 1
        #         elif distance < dist[n-1]:
        #             path[n-1] = 0
        #     neighbours = adj_list[node]
        #     for cur_node, wt in neighbours:
        #         if dist[node] + wt <= dist[cur_node]:
        #             dist[cur_node] = dist[node] + wt
        #             heapq.heappush(q, (dist[cur_node], cur_node))
                
                    
        # return path[n-1]


        adj_list = [[] for i in range(n)]
        for src, des, wt in roads:
            adj_list[src].append([des, wt])
            adj_list[des].append([src, wt])

        dist = [float("inf") for i in range(n)]
        path = [0 for i in range(n)]

        dist[0] = 0
        path[0] = 1

        q = [(0, 0)]
        mod = (10**9 + 7)
        while q:
            distance, node = heapq.heappop(q)
            neighbours = adj_list[node]
            for cur_node, wt in neighbours:
                new_distance = distance + wt
                
                if new_distance == dist[cur_node]:
                    path[cur_node] = (path[cur_node] + path[node])

                elif new_distance < dist[cur_node]:
                    dist[cur_node] = new_distance
                    heapq.heappush(q, (dist[cur_node], cur_node))
                    path[cur_node] = path[node]
                print(path, q, cur_node)

        
        return path[n-1] % mod


        # # Step 1️⃣: Build the adjacency list for the graph
        # adj = [[] for _ in range(n)]
        # for u, v, w in roads:
        #     adj[u].append([v, w])
        #     adj[v].append([u, w])
        
        # # Step 2️⃣: Initialize arrays to store shortest distance and number of ways
        # ways = [0] * n
        # ways[0] = 1
        # dis = [float("inf")] * n
        # dis[0] = 0
        
        # # Step 3️⃣: Min-heap to store (time, node)
        # heap = [(0, 0)]  # (current time, node)
        
        # while heap:
        #     time, node = heapq.heappop(heap)
            
        #     # Explore all neighbors of the current node
        #     for neighbor, travel_time in adj[node]:
        #         new_time = time + travel_time
                
        #         # Case 1️⃣: If we found another way with the same shortest time
        #         if new_time == dis[neighbor]:
        #             ways[neighbor] += ways[node]
                
        #         # Case 2️⃣: If we found a shorter time to reach the neighbor
        #         elif new_time < dis[neighbor]:
        #             dis[neighbor] = new_time
        #             heapq.heappush(heap, (new_time, neighbor))
        #             ways[neighbor] = ways[node]
        #         print(ways, heap, neighbor)
        
        # # Step 4️⃣: Return the number of ways to reach the destination modulo 10^9 + 7
        # MOD = 10**9 + 7
        # return ways[n-1] % MOD

n = 5
roads = [[0,1,1],[1,2,4],[0,4,3],[3,2,5],[3,4,1],[3,0,5],[1,3,1]]
sol = Graph()
print(sol.countPaths(n, roads))
