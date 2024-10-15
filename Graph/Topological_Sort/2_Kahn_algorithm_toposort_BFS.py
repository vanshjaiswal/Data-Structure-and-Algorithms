from collections import deque
class Graph:
    def topo_sort_bfs(self, V, adj):
        indegree = [0] * (V)
        ans =[]
        q=deque()

        for neigbours in adj:
            for i in range(len(neigbours)):
                indegree[neigbours[i]] += 1

        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(indegree[i])

        # if len(q)==0:
        #     return ans

        while q:
            node = q.popleft()
            neigbours = adj[node]
            ans.append(node)
            for cur_node in neigbours:
                indegree[cur_node] -= 1

            for i in range(len(indegree)):
                if indegree[i] == 0:
                    q.append(indegree[i])

        return ans






    