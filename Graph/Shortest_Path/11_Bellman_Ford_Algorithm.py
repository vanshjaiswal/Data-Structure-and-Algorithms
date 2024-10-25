class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellmanFord(self, V, edges, src):
        #code here
        dist = [float("inf") for i in range(V)]
        dist[src] = 0
        for _ in range(V-1):
            for u, v, wt in edges:
                if dist[u]!= float("inf")and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    
        #Check negative cycle
        for u,v,wt in edges:
            if dist[u]!= float("inf") and dist[u] + wt < dist[v]:
                return -1

        #If a node is not reachable then marking its distance as 10**8 
        for i in range(V):
            if dist[i] == float("inf"):
                dist[i] = 10**8
                    
        return dist