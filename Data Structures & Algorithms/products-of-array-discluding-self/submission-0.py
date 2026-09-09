class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        idx =-1
        n = len(nums)


        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
                if zero_count == 1:
                    idx = i
                else:
                    break
            else:
                product*= nums[i]

        if zero_count > 1:
            return [0]*n
        elif zero_count == 1:
            res = [0]*n
            res[idx] = product
            return res
        else:
            res = [0]*n
            for i in range(n):
                res[i] = product//nums[i]

            return res             