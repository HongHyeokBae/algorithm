

class Solution:
    def maxProfit(self, prices):
        """
        type prices: List[int]
        rtype: int
        """
        endsWithBuy = -prices[0]
        endsWithSell = 0

        for price in prices:
            buy = max(endsWithSell - price, endsWithBuy)
            sell = max(endsWithBuy + price, endsWithSell)
            endsWithBuy, endsWithSell = buy, sell

        return max(endsWithSell, endsWithBuy)

    def maxProfit_sol2(self, prices):
        if len(prices) <= 1:
            return 0

        priceSum = 0
        for i in range(1, len(prices)):
            if (prices[i] - prices[i - 1]) > 0:
                priceSum += prices[i] - prices[i - 1]

        return priceSum
