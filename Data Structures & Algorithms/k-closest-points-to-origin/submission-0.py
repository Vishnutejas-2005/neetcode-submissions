
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x,y in points:
            dis = x*x + y*y
            heapq.heappush(pq,(-dis,x,y))
            if len(pq) > k:
                heapq.heappop(pq)

        res = []

        while pq:
            d,x,y = heapq.heappop(pq)
            res.append([x,y])
        return res
