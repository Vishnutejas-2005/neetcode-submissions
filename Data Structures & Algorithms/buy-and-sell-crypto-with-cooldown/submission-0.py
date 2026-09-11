class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")
        sold = 0
        cooldown = 0

        for price in prices:
            h = max(hold,cooldown-price)
            s = hold + price
            c = max(cooldown,sold)

            hold = h
            sold = s
            cooldown = c

        return max(sold,cooldown)