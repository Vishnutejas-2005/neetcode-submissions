class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        import heapq

        count = Counter(tasks)
        pq = []

        for i in count.values():
            heapq.heappush(pq,-i)

        t = 0

        while pq:
            temp = []

            for _ in range(n+1):
                if pq:
                    freq = -heapq.heappop(pq)
                    freq -= 1
                    if freq > 0:
                        temp.append(freq)

                t += 1
                if not pq and not temp:
                    break
            for freq in temp:
                heapq.heappush(pq,-freq)

        return t