from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        while len(count)>0:
            m = min(count.keys())
            for _ in range(groupSize):
                count[m] -= 1
                if count[m] <0:
                    return False
                if count[m] == 0:
                    del count[m]
                m += 1

        return True