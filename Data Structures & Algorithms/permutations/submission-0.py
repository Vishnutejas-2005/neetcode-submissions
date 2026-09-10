class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def back(cl,cn,i):
            if i == n:
                res.append(cl)

            for j in range(n):
                if (cn&(1<<j)) == 0:
                    back(cl+[nums[j]],cn|(1<<j),i+1)

        back([],0,0)
        return res
