class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(nums,i,curr,n):
            if i == n:
                res.append(curr)
                return

            backtrack(nums,i+1,curr,n)
            backtrack(nums,i+1,curr+[nums[i]],n)
        backtrack(nums,0,[],len(nums))
        return res