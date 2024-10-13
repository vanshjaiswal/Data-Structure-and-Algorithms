class Graph:
    def adjacency_list(self, n, edges):
        adj_list={}
        for i in range(n+1):
            adj_list[i] = []

        for (i,j) in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        return adj_list

    def dfs_cycle(self, adj_list, visited_arr, node, parent):
        
        neighbours = adj_list[node]
        visited_arr[node] = 1
        for i in neighbours:
            if i==parent:
                continue
            if visited_arr[i] != 1:
                self.dfs_cycle(adj_list, visited_arr, i, node)
            else:
                return True 

        return False 

    def dfs_cycle_driver(self, n , edges):
        visited_arr = [0] * (n+1)
        adj_list = self.adjacency_list(n, edges)

        for node in range(1, n):
            if visited_arr[node] != 1:
                if self.dfs_cycle(adj_list, visited_arr, node, -1):
                    return True

        return False

edges = [(1,2), (1,3), (2,5), (6,7), (3,4), (3,6), (5,7)]
n=7

sol = Graph()

print(sol.dfs_cycle_driver(n, edges))