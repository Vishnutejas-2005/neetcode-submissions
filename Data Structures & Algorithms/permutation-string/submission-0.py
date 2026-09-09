from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)

        curr = Counter()

        k = len(s1)

        for r in range(len(s2)):
            curr[s2[r]] += 1

            if r >= k:
                curr[s2[r-k]] -= 1
                if curr[s2[r-k]] == 0:
                    del curr[s2[r-k]]

            if curr == count:
                return True

        return False