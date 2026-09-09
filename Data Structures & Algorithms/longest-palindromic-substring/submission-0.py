class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        max_len = 1
        start = 0
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                max_len = 2
                dp[i][i+1] = True
                start = i

        for l in range(2,n):
            i = 0
            j = l
            while 0 <= i < n and 0 <= j < n:
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    if max_len < l+1:
                        max_len = l + 1
                        start = i
                    
                i += 1
                j += 1

        return s[start:max_len+start]
