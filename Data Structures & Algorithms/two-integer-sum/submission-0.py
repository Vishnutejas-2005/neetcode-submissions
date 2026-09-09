class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            curr_target = target-nums[i]

            if d.get(curr_target,-1) != -1:
                return [d[curr_target],i]

            d[nums[i]] = i

        return []