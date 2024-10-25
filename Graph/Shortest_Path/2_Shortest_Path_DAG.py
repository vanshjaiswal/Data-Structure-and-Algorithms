from collections import deque
# edge = [[0,1,2],[0,2,1]]
class Graph:
    def adjacency_list_weighted(self, n, edges):
        adj_list = [[] for _ in range(n)]

        for source, destination, wt in edges:
            adj_list[source].append([destination, wt])

        return adj_list


    def topo_sort_dfs(self, node, visited_array, adj_list, stack):
        visited_array[node] = 1

        neighbours = adj_list[node]

        for cur_node, distance in neighbours:
            if visited_array[cur_node] != 1:
                self.topo_sort_dfs(cur_node, visited_array, adj_list, stack)

        stack.append(node)
        
        return stack 

    def topo_sort_dfs_driver(self, n, adj_list):
        visited_array = [0] * n
        stack = deque()

        for node in range(n):
            if visited_array[node] != 1:
                self.topo_sort_dfs(node, visited_array, adj_list, stack) 

        return list(stack)[::-1]

    def shortest_path_DAG(self, n, edges, src):
        adj_list = self.adjacency_list_weighted(n, edges)
        stack = self.topo_sort_dfs_driver(n, adj_list)

        dist = [float("inf") for _ in range(n)]
        dist[src] = 0

        for node in stack:
            neigbours = adj_list[node] #[[4, 2], [5,3]]
            for cur_node, wt in neigbours:
                if dist[node] + wt < dist[cur_node]:
                    dist[cur_node] = dist[node] + wt
        res=[-1 for _ in range(n)]
        for i in range(n):
            if dist[i] != float("inf"):
                res[i] = dist[i]
        return res

sol = Graph()
n = 4
m = 2
edge = [[0,1,2],[0,2,1]]

print(sol.shortest_path_DAG(n, edge, 0))





        
