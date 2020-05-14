

class Solution:
    def reverse(self, x):
        """
        type x: int
        rtype: int
        """
        result = 0
        symbol = 1 if x >= 0 else -1
        x = abs(x)
        INT_MIN, INT_MAX = pow(2,31), pow(2,31)-1

        while x:
            pop = x % 10
            if symbol == 1:
                if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7):
                    return 0
            else:
                if result > INT_MIN // 10 or (result == INT_MIN // 10 and pop > 8):
                    return 0
            
            result = result * 10 + pop
            x = x // 10

        return result * symbol
