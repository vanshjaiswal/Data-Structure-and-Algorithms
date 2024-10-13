"""
https://leetcode.com/problems/longest-common-subsequence/description/

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3


"""

class Solution:
    def tabulation(self, text1, text2):
        m=len(text1)
        n=len(text2)
        dp = [[-1 for j in range(n+1)] for i in range(m+1)]
        #base case: shift the index value by 1 to the right. so that we can conisder the -1 index ind<0 as 0
        # if ind1 < 0 or ind2 < 0:
        #     return 0
        """
        The above base case can be modified as
        if ind1 == 0 or ind2 == 0:
            return 0

        -1, 0, 1, 2, 3..... n-1
        0, 1, 2, 3, 4 .......n-1, n

        """
        for i in range(m+1):
            dp[i][0] = 0
        
        for j in range(n+1):
            dp[0][j] = 0

        #copy the recursion
        for ind1 in range(1, m+1):
            for ind2 in range(1, n+1):
                #match
                if text1[ind1-1] == text2[ind2-1]:
                    #here 1 signifies that we found 1 macthing character
                    dp[ind1][ind2] =  1 + dp[ind1-1][ind2-1]
                #not match case
                else:
                    dp[ind1][ind2] = max(dp[ind1][ind2-1], dp[ind1-1][ind2])


        i=n
        j=m
        ans = ""
        while i>0 and j>0:
            if text1[i-1] == text2[j-1]:
                ans = text1[i-1] + ans
                i-=1
                j-=1
            elif dp[i-1][j] > dp[j-1][i]:
                i-=1
            else:
                j-=1

        return ans

sol = Solution()
text1 = "abcde"
text2 = "bdgek" 

# ans =  sol.recursion(len(text1)-1, len(text2)-1, text1, text2)
# print(ans)

ans =  sol.tabulation(text1, text2)
print(ans)