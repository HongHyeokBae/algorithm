class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxprofit, minprice = 0, prices[0] 
        
        for i in prices:
            # minprice = min(minprice, i)
            if minprice > i:    minprice = i
            
            # maxprofit = max(maxprofit, i - minprice)
            if i - minprice > maxprofit:    maxprofit = i - minprice
        
        return maxprofit