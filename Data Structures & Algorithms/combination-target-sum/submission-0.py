class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(nums,i,cl,cs,n):
            if i >= n or cs > target:
                return
            if cs == target:
                res.append(cl)
                return

            backtrack(nums,i,cl+[nums[i]],cs+nums[i],n)
            backtrack(nums,i+1,cl,cs,n)

        backtrack(nums,0,[],0,len(nums))

        return res