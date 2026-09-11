class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        inf = 10**18
        dp = [inf]*(n+1)
        dp[0] = 0
        coins.sort()
        for i in range(n+1):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i],1+dp[i-coin])

        return dp[n] if dp[n] != inf else -1