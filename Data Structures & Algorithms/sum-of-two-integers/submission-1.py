class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            xor = (a^b)&mask
            an = ((a&b)<<1)&mask
            a = xor
            b = an

        if a <= 0x7FFFFFFF:
            return a

        return a - 0x100000000