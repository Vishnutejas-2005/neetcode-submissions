class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while n != 1:
            s = n
            curr = 0
            while s:
                rem = s%10
                curr += rem*rem
                s = s//10
            if curr in d:
                return False
            d.add(curr)
            n = curr

        return True