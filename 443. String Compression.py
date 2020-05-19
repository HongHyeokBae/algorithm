

class Solution:
    def compress(self, chars):
        """
        type chars: List[str]
        rtype: int
        """
        count, write = 1, 0

        for i in range(1, len(chars) + 1):
            if  i == len(chars) or chars[i] != chars[i - 1]:
                chars[write] = chars[i - 1]
                write += 1
                write = self.writeDigits(chars, write, count)
                count = 1
            else:
                count += 1
        
        return write

    def writeDigits(self, chars, write, count):
        if count > 1:
            for n in str(count):
                chars[write] = n
                write += 1
        
        return write