

class Solution:
    def multiply(self, num1, num2):
        """
        type num1: str
        type num2: str
        rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]
        num = [0] * (len(num1) + len(num2))

        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                num[i+j] += int(n1) * int(n2)
                num[i+j+1] += num[i+j] // 10
                num[i+j] = num[i+j] % 10

        result, leadingZero = "", True
        for n in num[::-1]:
            if leadingZero and n != 0:
                leadingZero = False
                
            if not leadingZero:
                result += str(n)

        return result


