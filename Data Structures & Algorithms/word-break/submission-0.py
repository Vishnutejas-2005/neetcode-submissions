class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        m = max(len(word) for word in wordDict)

        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1,n+1):
            for j in range(1,min(m,i)+1):
                if s[i-j:i] in wordDict and dp[i-j]:
                    dp[i] = True
                    break

        return dp[n]
                    
