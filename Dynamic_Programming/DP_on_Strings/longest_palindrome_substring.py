class Solution:
    def longestPalindrome(self, s):
        s1=s
        s2=s1[::-1]

        m=len(s)
        n=len(s)

        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        #base case if i<0 or j <0 return 0
        for j in range(m+1):
            dp[0][j] = 0

        for i in range(m+1):
            dp[i][0] = 0

        ans = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                #match
                if  s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                ans = max(dp[i][j], ans)

        print(dp)
        i =  m
        j = n    
        ans = ""

        while i>0 and j>0:
            if s1[i-1]==s2[j-1]:
                ans += s1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        return ans

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str


class Solution:
    def largestPalindrome(self, s: str, l: int, r: int) -> str:  
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l + 1:r]
    
    def longestPalindrome(self, s: str) -> str:
        # generate the substrings
        n = len(s)
        longest = ""
        
        # view each point as the center and expand
        for center in range(n):
            odd = self.largestPalindrome(s, center, center)
            even = self.largestPalindrome(s, center, center + 1)
            if len(longest) < len(odd):
                longest = odd
            
            if len(longest) < len(even):
                longest = even
                
        return longest


sol = Solution()
s="aacabdkacaa"
s1="aacakdbacaa"

s="babad"
s1="dabab"
ans = sol.longestPalindrome(s)
print(ans)

"""
[[0, 0, 0, 0, 0, 0], 
[0, 0, 0, 1, 0, 1], 
[0, 0, 1, 0, 2, 0], 
[0, 0, 0, 2, 0, 3], 
[0, 0, 1, 0, 3, 0], 
[0, 1, 0, 0, 0, 0]]



     a  a  c  a  k  d  b  a  c  a  a
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
a[0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1], 
a[0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 1, 2], 
c[0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0], 
a[0, 1, 1, 0, 4, 0, 0, 0, 1, 0, 3, 1], 
b[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
d[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
k[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
a[0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1], 
c[0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0], 
a[0, 1, 1, 0, 3, 0, 0, 0, 1, 0, 3, 1], 
a[0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 1, 4]]



aaca"""