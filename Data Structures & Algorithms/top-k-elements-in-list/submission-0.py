from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        pq = []

        for key,val in c.items():
            heapq.heappush(pq,(-val,key))

        res = []

        while pq and len(res) < k:
            _,val = heapq.heappop(pq)
            res.append(val)

        return res
