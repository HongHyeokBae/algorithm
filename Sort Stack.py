

class Solution:
    def sortStack(self, stack):
        """
        type stack: List[int]
        rtype: None
        """
        for i in range(len(stack)):
            stack[i:] = self.findMax(stack[i:])

        print(stack)
    
    def findMax(self, s1):
        temp = []
        maxValue = s1.pop()

        while s1:
            popped = s1.pop()
            if popped > maxValue:
                temp.append(maxValue)
                maxValue = popped
            else:
                temp.append(popped)
        
        s1.append(maxValue)
        s1.extend(temp)
        return s1
    
    def sortStack_sol2(self, stack):
        sort = []
        while stack:
            tmp = stack.pop()
            while sort and sort[-1] > tmp:
                stack.append(sort.pop())
            sort.append(tmp)
        
        stack.extend(sort)
        print(stack)

s = Solution()
s.sortStack_sol2([2,1,4,3])
