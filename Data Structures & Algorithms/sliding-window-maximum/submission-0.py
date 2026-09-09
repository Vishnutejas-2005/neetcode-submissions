from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = Counter(nums[:k])
        res = [max(count.keys())]

        for i in range(k,n):
            count[nums[i]] += 1

            count[nums[i-k]] -= 1
            if count[nums[i-k]] == 0:
                del count[nums[i-k]]

            res.append(max(count.keys()))

        return res