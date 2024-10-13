"""
https://leetcode.com/problems/number-of-provinces/

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2


"""
from collections import deque
class Solution:

    def adjacency_list(self, isConnected):
        adj_list = {}
        n= len(isConnected)
        for i in range(n):
            adj_list[i] = []

        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    adj_list[i].append(j)

        return adj_list

        
    def dfs(self,node, adj_list, visited_array, ans):
        ans.append(node)
        visited_array[node] = 1

        neighbours = adj_list[node]

        for i in neighbours:
            if visited_array[i] != 1:
                self.dfs(i, adj_list, visited_array, ans)

        return ans, visited_array


    def bfs(self, node, adj_list, visited_array):
        q = deque()
        q.append(node)
        ans = []
        visited_array[node] = 1

        while q:
            node = q.popleft()
            ans.append(node)
            neighbours = adj_list[node]
            for i in neighbours:
                if visited_array[i] != 1:
                    q.append(i)
                    visited_array[i] =1


        return ans, visited_array

        

    def findCircleNum(self, isConnected):

        adj_list = self.adjacency_list(isConnected)
        print(adj_list)
        n= len(isConnected)
        ans = []
        #dfs
        count = 0
        visited_array = [0] * (n)

        for i in range(n): #0,1,2
            print(visited_array)
            if visited_array[i] != 1:
                count += 1
                # self.dfs(i, adj_list, visited_array, ans)
                self.bfs(i, adj_list, visited_array)

        return count



    


sol = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# isConnected = [[1,0,0],[0,1,0],[0,0,1]]
ans = sol.findCircleNum(isConnected=isConnected)
print(ans)