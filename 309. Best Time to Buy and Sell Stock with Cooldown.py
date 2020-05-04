class Solution:
    def maxProfit(self, prices):
        """
        type prices: List[int]
        rtype: int
        """
        buy, sell = [0] * len(prices), [0] * len(prices)
        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            sell[i] = max(buy[i - 1] + price, sell[i - 1])
            buy[i] = max(sell[i - 2] - price if i > 2 else -price, buy[i - 1])

        return sell[-1]