

class Solution:
    def change(self, amount, coins):
        """
        type amount: int
        type coins: List[int]
        rtype: int
        """
        numOfChanges = [0] * (amount + 1)
        numOfChanges[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                numOfChanges[i] += numOfChanges[i - coin]
        
        return numOfChanges[amount]