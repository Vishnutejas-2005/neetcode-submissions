class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for l in range(2,n+1):
            i = 0
            j = l

            while i < n and j <n:
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j],dp[i][k]+nums[i]*nums[k]*nums[j]+dp[k][j])
                i += 1
                j += 1

        return dp[0][n-1]