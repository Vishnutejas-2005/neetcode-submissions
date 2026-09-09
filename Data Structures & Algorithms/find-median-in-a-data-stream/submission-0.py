import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        if self.small and self.big and (-self.small[0] > self.big[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big,val)

        if len(self.small) > 1 + len(self.big):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.big,val)

        elif len(self.big) > 1 + len(self.small):
            val = heapq.heappop(self.big)
            heapq.heappush(self.small,-val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]

        if len(self.big) > len(self.small):
            return self.big[0]

        return (-self.small[0] + self.big[0])/2 
        
        