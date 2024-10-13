class Solution:
    def fibonacci(self, n):
        if n<=1:
            return n
        #step 1: Initialize the DP
        dp=[-1]*(n+1)

        #step 2 set the base case
        dp[0] = 0
        dp[1] = 1

        # step 3: Now convert the recursive function f(n-1) + f(n-2) into dp
        # using for loop. n=1 and n=0 is already handled. This recursive function will 
        # we called when n > 2

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


if __name__ == "__main__":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    sol = Solution()
    n=5
    ans = sol.fibonacci(n)
    print(ans)
        