from collections import deque

class Graph:
    #starting at Node 0
    def BFS(self, n, edges):
        adj_list = self.adjacency_list(n, edges)
        bfs= []
        visited_array = [0] * (n+1) 
        q = deque()
        q.append(0)
        visited_array[0] = 1

        while q:
            node = q.popleft()
            bfs.append(node)
            neighbours = adj_list[node]

            for i in neighbours:
                if visited_array[i] != 1:
                    visited_array[i] =1
                    q.append(i)

        return bfs

    def adjacency_list(self, n, edges):
        adj_list = {}
        for i in range(n+1):
            adj_list[i] = []

        for (i,j) in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        return adj_list

