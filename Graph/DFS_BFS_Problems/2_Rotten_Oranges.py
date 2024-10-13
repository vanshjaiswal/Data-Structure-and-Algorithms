"""
https://leetcode.com/problems/rotting-oranges/description/

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.


Input: grid = [[2,1,1],
                [1,1,0],
                [0,1,1]]
Output: 4

"""
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count_fresh_oranges = 0
        # count=0
        m=len(grid)
        n=len(grid[0])
        visited = grid
        q=deque()

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    count_fresh_oranges += 1
                if visited[i][j]==2:
                    q.append((i,j))

        if count_fresh_oranges == 0:
            return 0
        if not q:
            return -1
#Anyone confused with why minutes =-1?
# The answer is do dry run on your own to get the feel
# Otherwise for the spoon feeders you take out current rotten oranges and add their neighbours in the queue in every iteration.By the time you've rotten all the oranges. Your queue still has last set of rotten oranges, your answer is found at this stage but the loop will run one more time to empty the queue and come out. But in this extra iteration your minutes increases by 1. Either return minutes -1 or initialize minutes to -1, to get the correct answer
        time_taken = -1
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while q:
            size = len(q)
            while size > 0:
                size -= 1
                x, y = q.popleft()
                for dx, dy in dirs:
                    i = x + dx
                    j = y + dy
                    if 0 <= i < m and 0 <= j < n and visited[i][j]==1:
                        visited[i][j] = 2
                        count_fresh_oranges -= 1
                        q.append((i,j))

            time_taken += 1

        if count_fresh_oranges == 0:
            return time_taken
        return -1


        

        

        
