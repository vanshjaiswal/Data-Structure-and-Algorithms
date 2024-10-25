from collections import deque
class Graph:
    def djikstra_algo(self, n, src, edges):
        adj_list = self.adjacency_list_weighted(n,edges)
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        parent = [i for i in range(n)]

        priority_queue = []

        priority_queue.append((0, src))

        while priority_queue:
            
            distance, node = priority_queue.pop(0)
            neighbours = adj_list[node]

            for cur_node, wt in neighbours:
                if dist[node] + wt < dist[cur_node]:
                    dist[cur_node] = dist[node] + wt
                    # print(dist)
                    priority_queue.append((dist[node]+wt, cur_node))
                    parent[cur_node] = node

            priority_queue = sorted(priority_queue)


        destination_distance = dist[n-1]
        path=[]
        path.append(n-1)
        cur_parent = n-1
        while destination_distance != 0:
            path.append(parent[cur_parent])
            cur_parent = parent[cur_parent]
            destination_distance = dist[cur_parent]
        
        return path[::-1]

    def adjacency_list_weighted(self, n, edges):
        adj_list = [[] for i in range(n)]
        for src, dest, wt in edges:
            adj_list[src].append((dest, wt))
        
        return adj_list


edges = [(0,1,4), (0,2,4), (1,0,4), (1,2,2), (2,0,4), (2,1,2), (2,3,3),(2,5,6),(2,4,1),
(3,2,3), (3,5,2),(4,2,1),(4,5,3),(5,2,6),(5,3,2),(5,4,3)]
src = 0
n=6
 

sol = Graph()
print(sol.djikstra_algo(n,src,edges))
