class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <=2:
            return max(nums)
        def rob_linear(arr):
            n = len(arr)
            if n <= 2:
                return max(arr)

            prev2 = arr[0]
            prev1 = max(arr[0],arr[1])

            for i in range(2,n):
                curr = max(prev1,prev2+arr[i])
                prev2 = prev1
                prev1 = curr


            return prev1

        return max(rob_linear(nums[1:]),rob_linear(nums[:-1]))

         
            