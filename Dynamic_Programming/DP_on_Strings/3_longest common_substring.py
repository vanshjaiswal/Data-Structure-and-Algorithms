"""
Substring are consecutives

Input: str1 = "ABCDGH", str2 = "ACDGHR"
Output: 4
Explanation: The longest common substring is "CDGH" which has length 4.


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
        ans=0
        #copy the recursion
        for ind1 in range(1, m+1):
            for ind2 in range(1, n+1):
                #match
                if text1[ind1-1] == text2[ind2-1]:
                    #here 1 signifies that we found 1 macthing character
                    dp[ind1][ind2] =  1 + dp[ind1-1][ind2-1]
                #not match case
                else:
                    dp[ind1][ind2] = 0
                
                ans = max(ans, dp[ind1][ind2])

        return ans

sol = Solution()
text1 = "ABCDGH"
text2 = "ACDGHR" 



#string match
text1 = "leetcode"
text2 = "etco"


text1 = "park"
text2 = "spake"
ans =  sol.tabulation(text1, text2)
val = (len(text1) - ans ) +  (len(text2) - ans)
print(val)