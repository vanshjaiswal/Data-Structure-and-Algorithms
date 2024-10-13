"""
If we closely look at the relation f(n) = f(n-1) + f(n-2) the value of f(n)
depends on the last 2 values so we need not to use the array and we can simply calculate 
last two values from the base case and the loop

"""

class Solution:
    def fibonacci(self, n):
        if n<=1:
            return n
        prev = 1
        prev2 = 0

        for i in range(2, n+1):
            cur_i = prev + prev2
            prev2 = prev
            prev = cur_i
        return prev


if __name__ == "__main__":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    sol = Solution()
    n=5
    ans = sol.fibonacci(n)
    print(ans)
        