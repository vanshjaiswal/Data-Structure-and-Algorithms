"""
https://leetcode.com/problems/course-schedule/

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 

Input : [[0,1], [2,0]]


"""

from collections import deque
class Graph:

    def adjacency_list(self, numCourses, prerequisites):
        adj_list = [[] for i in range(numCourses)]
        # for i in range(numCourses):
        #     adj_list[i] = []

        for course in prerequisites:
            adj_list[course[1]].append(course[0])

        return adj_list





    def canFinish(self, numCourses: int, prerequisites):
        adj_list = self.adjacency_list(numCourses, prerequisites)

        q=deque()
        indegree = [0] * numCourses
        ans= []

        for neigbours in adj_list:
            for i in range(len(neigbours)):
                indegree[neigbours[i]] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        # print(q)

        while q:
            node = q.popleft()
            neigbours = adj_list[node]
            ans.append(node)

            for cur_node in neigbours:
                indegree[cur_node] -= 1
                if indegree[cur_node] == 0:
                    q.append(cur_node)
        
        if len(ans) ==  numCourses:
            return ans
        return []

sol = Graph()
prerequisites = [[0,1], [2,0]]
numCourses = 3


[[1,0],[1,2],[0,1]]

print(sol.canFinish(numCourses, prerequisites))