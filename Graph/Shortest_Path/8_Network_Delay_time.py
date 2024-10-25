"""
https://leetcode.com/problems/network-delay-time/description/



"""

from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n+1)]
        for src, dst, wt in times:
            adj_list[src].append([dst, wt])

        time_mat = [float("inf") for _ in range(n+1)]
        time_mat[k] = 0
        q=deque()
        #q.append(time, node)
        q.append((0, k))
        while q:
            time, node = q.popleft()
            neighbours = adj_list[node]
            for cur_node, cur_time in neighbours:
                if time + cur_time < time_mat[cur_node]:
                    time_mat[cur_node] = time + cur_time
                    q.append((time+cur_time, cur_node))

        mx = float("-inf")
        for i in range(1, n+1):
            if time_mat[i] != float("inf"):
                mx = max(mx, time_mat[i])
            else:
                return -1

        return mx

        