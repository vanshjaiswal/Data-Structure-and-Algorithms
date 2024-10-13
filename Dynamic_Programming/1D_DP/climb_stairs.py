"""
https://leetcode.com/problems/climbing-stairs/description/


You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


We have two choices at every index. we can jump 1 or 2. so f(n-1) +  f(n-2)

as the problem statement asks for the count we will return the sum of all choices

when we are at 0 there is only 1 step when we are at 1 then also 1 step
"""

class Solution:
    def recursion_stairs(self, n):
        if n<=1:
            return 1

        return self.recursion_stairs(n-1)  + self.recursion_stairs(n-2)

    def memoization_stairs(self, n, dp):
        if n<=1:
            return 1

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.memoization_stairs(n-1, dp) + self.memoization_stairs(n-2, dp)

        return dp[n]

    def memoization_driver(self, n):
        dp=[-1] * (n+1)
        output = self.memoization_stairs(n, dp)
        return output


    def tabularization_stairs(self, n):
        if n<=1:
            return 1

        dp = [-1] * (n+1)

        dp[0]=1
        dp[1]=1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    def space_optimized_stairs(self, n):
        if n<=1:
            return 1
        
        prev = 1
        prev2 = 1

        for i in range(2, n+1):
            cur_i = prev + prev2
            prev2 = prev
            prev = cur_i

        return prev

if __name__ == "__main__":
    sol = Solution()
    n=5
    ans = sol.recursion_stairs(n)
    print("Recursion: ", ans)

    
    ans = sol.memoization_driver(n)
    print("Memoization: ", ans)

   
    ans = sol.tabularization_stairs(n)
    print("tabularization: ", ans)

    ans = sol.space_optimized_stairs(n)
    print("space_optimized: ", ans)