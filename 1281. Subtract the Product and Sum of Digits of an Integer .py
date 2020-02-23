import math

# Array
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        i = 0
        while True:
            mulOfTen = math.pow(10, i)
            if n // mulOfTen == 0:
                break
            
            digits = (n // mulOfTen) % 10
            p = p * digits
            s = s + digits
            i = i + 1
        
        return int(p - s)
            