from collections import deque

class Graph:
    #starting at Node 0
    def DFS(self, node, dfs, visited_array, adj_list):
        dfs.append(node)
        visited_array[node] = 1
        neighbours = adj_list[node]
        for i in neighbours:
            if visited_array[i] != 1:
                self.DFS(i, dfs, visited_array, adj_list)


        return dfs

    def dfs_driver(self, n, edges):
        adj_list = self.adjacency_list(n, edges)
        dfs = [0]
        visited_array = [0] * (n+1)
        # visited_array[0] = 1

        return self.DFS(0, dfs, visited_array, adj_list)

    def adjacency_list(self, n, edges):
        adj_list = {}
        for i in range(n+1):
            adj_list[i] = []

        for (i,j) in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        return adj_list

