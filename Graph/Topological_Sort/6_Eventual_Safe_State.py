"""
https://leetcode.com/problems/find-eventual-safe-states/description/


"""

from collections import deque
class Solution:
    def adjacency_list(self, graph):
        adj_list = [[] for i in range(len(graph))]

        for i, ls in enumerate(graph):
            for j in ls:
                adj_list[j].append(i)
        return adj_list




    def eventualSafeNodes(self, graph):
        adj_list = self.adjacency_list(graph)
        ans= []

        n=len(graph)
        indegree = [0] * (n)
        q=deque()

        for neighbours in adj_list:
            for i in range(len(neighbours)):
                indegree[neighbours[i]] += 1
        
        for i in range(n):
            if indegree[i] ==  0:
                q.append(i)

        while q:
            node = q.popleft()
            neighbours = adj_list[node]

            ans.append(node)

            for cur_node in neighbours:
                indegree[cur_node] -= 1
                if indegree[cur_node] == 0 :
                    q.append(cur_node)
        
        return sorted(ans)


        