

class Solution:
    def plusOne(self, digits):
        """
        type digits: List[int]
        rtype: List[int]
        """
        result = []
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            result.append((digits[i]+carry)%10)
            if digits[i] + carry > 9:
                carry = 1
            else:
                carry = 0
        if carry:
            result.append(carry)

        return result