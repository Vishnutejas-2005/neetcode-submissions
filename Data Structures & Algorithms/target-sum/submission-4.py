class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        maxi = max(nums)
        dp = {i:0 for i in range(-s-maxi,s+1+maxi)}

        dp[0] = 1
        for num in nums:
            dummy = dp.copy()
            for j in range(-s,s+1):
                dp[j] = dummy[j+num] + dummy[j-num]
        if -s<=target<=s:
            return dp[target]
        return 0