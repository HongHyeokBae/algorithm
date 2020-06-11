

class Solution:
    def generateParenthesis(self, n):
        """
        type n: int
        rtype: List[str]
        """
        result = []
        self.genParens(n, n, "", result)

        return result

    def genParens(self, leftOpens, leftCloses, res, result):
        if leftOpens == 0 and leftCloses == 0:
            result.append(res)
        
        if leftOpens > 0:
            self.genParens(leftOpens - 1, leftCloses, res + "(", result)
        if leftOpens < leftCloses:
            # append ')' only when there are more '(' than ')'
            self.genParens(leftOpens, leftCloses - 1, res + ")", result)