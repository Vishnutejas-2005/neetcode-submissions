class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign = -1
        x = int(str(sign*x)[::-1])

        if x >= 1<<31 or x < -(1<<31):
            return 0

        return sign*x