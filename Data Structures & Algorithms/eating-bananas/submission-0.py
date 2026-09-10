class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = -1

        while left <= right:
            mid = (left+right)//2
            curr = 0

            for i in piles:
                curr += (i+mid-1)//mid

            if curr > h:
                left = mid + 1
            else:
                res = mid
                right = mid-1

        return res