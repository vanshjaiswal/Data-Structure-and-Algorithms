#shortest path for undirected graph with unit weights

from collections import deque
class Graph:
    def adjacency_list(self, n, edges):
        adj_list = {}
        for i in range(n):
            adj_list[i] = []

        for (i,j) in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        return adj_list


    def shortest_path(self, edges, n, m, src):
        adj_list = self.adjacency_list(n, edges)
        distance_array = [float("inf") for _ in range(n)]

        result = [-1 for _ in range(n)]

        q = deque()

        q.append(src)
        distance_array[src] = 0

        while q:
            
            node = q.popleft()
            neighbours = adj_list[node]

            for cur_node in neighbours:
                if distance_array[node] + 1 < distance_array[cur_node]:
                    distance_array[cur_node] = distance_array[node] + 1
                    q.append(cur_node)


                 
        
        for i in range(n):
            if distance_array[i] != float("inf"):
                result[i]=distance_array[i]

        return result

sol =Graph()
n = 9
m = 10
edges=[[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
src=0

print(sol.shortest_path(edges,n, m, src))


