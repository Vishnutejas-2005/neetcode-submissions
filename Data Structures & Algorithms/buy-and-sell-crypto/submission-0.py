class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        mini = prices[0]
        n = len(prices)
        for i in range(1,n):
            if mini < prices[i]:
                max_profit = max(max_profit,prices[i]-mini)
            else:
                mini = prices[i]

        return max_profit
