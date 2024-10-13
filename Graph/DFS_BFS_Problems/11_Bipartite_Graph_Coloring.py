class Graph:
    def adjacency_list(self, n, edges):
        adj_list={}
        for i in range(n+1):
            adj_list[i] = []

        for i, ls in enumerate(edges):
            for j in range(len(ls)):
                adj_list[i].append(ls[j])
            
        # print(adj_list)
        return adj_list

    def coloring_dfs(self, adj_list, color_list, node, color):

        color_list[node] = color

        neighbours = adj_list[node]

        for current_node in neighbours:
            if color_list[current_node] == -1:
                # color_list[current_node] = not color
                if not self.coloring_dfs(adj_list, color_list, current_node, 1-color):
                    return False
            elif color_list[current_node] == color:
                return False
  

        return True

    def dfs(self, node, col, color, adj):
        color[node] = col
        
        # Traverse adjacent nodes
        for it in adj[node]:
            # If uncolored
            if color[it] == -1:
                if not self.dfs(it, 1 - col, color, adj):
                    return False
            # If previously colored and have the same color
            elif color[it] == col:
                return False
        
        return True

    def coloring_driver(self, n, edges):
        adj_list = self.adjacency_list(n, edges)
        color_list = [-1] * (n)
        # color_list[0] = True

        for node in range(n):
            if color_list[node] == -1:
                if not(self.coloring_dfs(adj_list, color_list, node, 0)):
                    return False

        return True

edges = [[1,2,3],[0,2],[0,1,3],[0,2]]
n=4

sol = Graph()

print(sol.coloring_driver(n, edges))
