class Solution:
    def recursion_frog_jump(self, index, H):
        #base case: If frog is at index 0 then he can not jump so energy will be 0
        if index == 0:
            return 0

        #Frog can take either one step or two step so we will try to find all the
        #possible choices using recursion then we will find the minimum. 
        #here we can use left and right recursion approach for 1 and 2 steps. 

        #jump 1 step: we will add the energy in reaching n-1 step
        right = float("inf")
        left = self.recursion_frog_jump(index-1, H) + abs(H[index]-H[index-1])

        #jump 2 step: one conition if index < 2 then frogm can not jump 2 step

        if index>1:
            right = self.recursion_frog_jump(index-2, H) + abs(H[index]-H[index-2])

        #return the minimum of left and right
        return min(left, right)


    def memoization_frog(self, n, H, dp):
        if n == 0:
            return 0 
        
        if dp[n] != -1:
            return dp[n]

        right = float("inf")
        left = self.memoization_frog(n-1, H, dp) + abs(H[n]-H[n-1])

        if n>1:
            right = self.memoization_frog(n-2, H, dp) + abs(H[n]-H[n-2])

        dp[n] = min(left, right)

        return dp[n]

    def memoization_driver_frog(self, H, n):
        dp = [-1]*(n+1)
        result = self.memoization_frog(n-1, H, dp)
        return result



    #tabular DP:
    def tabular_frog(self, H, n):
        if n==0:
            return 0

        dp = [-1] * (n+1)

        dp[0] = 0
        right=float("inf")
        #In tabulation we to replace f(n-1) from recursion/memoization to dp[n-1]
        for i in range(1, n):
            left = dp[i-1] + abs(H[i]-H[i-1])
            if i > 1:
                right = dp[i-2] + abs(H[i]-H[i-2])
            
            dp[i] = min(left, right)

        return dp[n-1]

    # Space optimization
    def space_optimized_frog(self, H, n):
        if n==0:
            return 0
        prev2 = 0
        prev = 0
        right=float("inf")
        for i in range(1, n):
            left = prev + abs(H[i]-H[i-1])
            if i > 1:
                right = prev2 + abs(H[i]-H[i-2])

            cur_i = min(left, right)
            prev2 = prev
            prev = cur_i

        return prev
            



if __name__ == "__main__":
    sol = Solution()
    H = [10,20,30,10]
    n=len(H)
    ans = sol.recursion_frog_jump(n-1, H)
    print("Recursion: ", ans)

    ans = sol.memoization_driver_frog(H, n)
    print("Memoization: ", ans)

    ans = sol.tabular_frog(H, n)
    print("Tabulation: ", ans)

    ans = sol.space_optimized_frog(H, n)
    print("space_optimized: ", ans)