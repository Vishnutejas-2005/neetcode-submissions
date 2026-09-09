class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0

        s = set(nums)

        for i in s:
            if i-1 not in s:
                curr = 0
                num = i
                while num in s:
                    curr += 1
                    num +=1
                long = max(long,curr)

        return long 