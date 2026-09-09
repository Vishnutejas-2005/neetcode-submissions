import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heapq.heappush(pq,-stone)

        while len(pq) >= 2:
            a = -heapq.heappop(pq)
            b = -heapq.heappop(pq)

            if a != b:
                heapq.heappush(pq,b-a)

        if len(pq) == 0:
            return 0
        else:
            return -pq[0]
