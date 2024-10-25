"""
https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimum-multiplications-to-reach-end

STRIVER'S QUESTION

MOST IMPORTANT AND TRICKY


Given start, end and an array arr of n numbers. At each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.

Your task is to find the minimum steps in which end can be achieved starting from start. If it is not possible to reach end, then return -1.

Sol:
Use Dijsktra. Convert the problem into the graph. How ?  after every multiplication the result will be the node and steps will be the wt from src --> node (steps=wt)

How many node?
0----> 10**5 -1 because of modulo
"""
from collections import deque
class Graph:
    def min_steps(self, arr, start, end):
        dist = [float("inf") for i in range(10**5)]
        dist[start] = 0
        q = deque()
        q.append((0, start))

        while q:
            steps, node = q.popleft()

            for i in range(len(arr)):
                new_node = (node * arr[i]) % (10**5)
                new_steps = steps + 1
                if new_steps < dist[new_node]:
                    dist[new_node] = new_steps
                    if (new_node == end):
                        return steps + 1
                    q.append((new_steps, new_node))
                    
        if dist[new_node] != float("inf"):
            return dist[new_node]
        return -1


sol=Graph()
arr = [2, 5, 7]
start = 3
end = 30

print(sol.min_steps(arr, start, end))
