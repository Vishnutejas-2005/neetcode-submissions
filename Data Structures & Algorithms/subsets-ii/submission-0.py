class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n =  len(nums)

        res = []

        def back(cl,i):
            res.append(cl)

            for j in range(i,n):
                if j > i and nums[j] == nums[j-1]:
                    continue

                back(cl+[nums[j]],j+1)

        back([],0)
        return res