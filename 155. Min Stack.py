

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, x):
        """
        type x: int
        rtype: None
        """
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)

    def pop(self):
        """
        rtype: None
        """
        curr = self.stack.pop()
        if curr == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        """
        rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        rtype: int
        """
        return self.minStack[-1]