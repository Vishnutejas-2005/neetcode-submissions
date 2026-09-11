class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        far = 0
        curr_end = 0

        for i in range(len(nums)-1):
            far = max(far,i+nums[i])
            if curr_end == i:
                jumps += 1
                curr_end = far

        return jumps
