"""
n=3 and arr[]= [[1,2,5],[3,1,1],[3,3,3]]

https://www.geeksforgeeks.org/problems/geeks-training/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geeks-training
"""

class Solution:
    def max_points_recursion(self, days, last, arr):
        if days == 0:
            maximum = 0
            for i in range(3):
                if i != last:
                    maximum = max(maximum, arr[0][i])
            return maximum

        maxi = 0
        for i in range(3):
            if i != last:
                activity = arr[days][i] + self.max_points_recursion(days-1, i, arr)
                maxi = max(activity, maxi)
                
        return maxi

    def max_ninja(self, arr, n):
        last = 3
        output = self.max_points_recursion(n-1, last, arr)
        return output


    def memoization(self, days, last, arr, dp):
        if days == 0:
            maximum = 0
            for i in range(3):
                if i != last:
                    maximum = max(maximum, arr[0][i])
            return maximum

        if dp[days][last] != -1:
            return dp[days][last]

        maxi = 0
        for i in range(3):
            if i != last:
                activity = arr[days][i] + self.memoization(days-1, i, arr, dp)
                maxi = max(activity, maxi)
        dp[days][last] = maxi
        return dp[days][last]

    def memoization_driver(self, arr, n):
        #Here for every day we have  possible values of last so we need N * 4 dp
        dp=[[-1 for j in range(4)] for i in range(n)]
        last =3
        output = self.memoization(n-1, last, arr, dp)
        return output  


    def tabulation(self, arr, n):
        dp = [[-1 for j in range(4)] for i in range(n)]
        
        #we are going to have 4 values of last at day=0 base case, last = 0,1,2,3
        dp[0][0] = max(arr[0][1], arr[0][2])
        dp[0][1] = max(arr[0][0], arr[0][2])
        dp[0][2] = max(arr[0][0], arr[0][1])
        dp[0][2] = max(arr[0][0], arr[0][1], arr[0][2])

        #iterate over days
        for days in range(1, n):
            #each day we have 4 value of last
            for last in range(4):
                dp[days][last]=0
                #we have to select a particular task out of three task, recursion block
                for task in range(3):
                    if task != last:
                        points = arr[days][task]  + dp[days-1][task]
                        dp[days][last] = max(dp[days][last], points)
                
        return dp[n-1][3]

    def space_optimized(self, arr, n):
        prev = [0] * 4

        prev[0] = max(arr[0][1], arr[0][2])
        prev[1] = max(arr[0][0], arr[0][2])
        prev[2] = max(arr[0][0], arr[0][1])
        prev[2] = max(arr[0][0], arr[0][1], arr[0][2])

        for days in range(1, n):
            temp = [0] * 4
            for last in range(4):
                temp[last] = 0
                for task in range(3):
                    if task != last:
                        activity = arr[days][task] + prev[task]
                        temp[last] = max(temp[last], activity)
            prev = temp

        return prev[3] 

                




sol = Solution()
arr = [[1,2,5],[3,1,1],[3,3,3]]
n=3
ans = sol.max_ninja(arr, n)
print(ans)

ans = sol.memoization_driver(arr, n)
print(ans)

ans = sol.tabulation(arr, n)
print(ans)

ans = sol.space_optimized(arr, n)
print(ans)