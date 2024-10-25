"""

https://takeuforward.org/data-structure/floyd-warshall-algorithm-g-42/

"""

class Graph:
    def floyd_warshall(self, n, edges):
        #creating the adjacency matrix
        adj_matrix = [[float("inf") for _ in range(n)] for j in range(n)]
        #for directed graph
        for src, des, wt in edges:
            adj_matrix[src][des] = wt
            #For undirected graphs:
            #adj_mat[des][src] = wt

        #Floyd warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj_matrix[i][j] = min(adj_matrix[i][j] , (adj_matrix[i][k] + adj_matrix[k][j]))

        #This adj matrix will store the shortest path between each node. 

        #check the negative cycle. 
        #If a node is taking -ve path value then the graph have negative cycle.
        for i in range(n):
            if adj_matrix[i][i] < 0:
                return -1 #-1 represents the negative cycle

        return adj_matrix
