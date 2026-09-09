import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.curr = 0
        self.arr = []
        for i in nums:
            self.add(i)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.arr,val)
        self.curr += 1
        while self.curr > self.k:
            heapq.heappop(self.arr)
            self.curr -= 1

        return self.arr[0]

