class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount
        m = len(coins)

        inf = 10**18
        dp = [[0 for _ in range(m+1)]for _ in range(n+1)]

        for j in range(m+1):
            dp[0][j] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if i >= coins[j-1]:
                    dp[i][j] = dp[i-coins[j-1]][j]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[n][m]
