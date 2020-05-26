

class MyQueue: 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackNewest = []
        self.stackOldest = []

    def push(self, x: int):
        """
        Push element x to the back of queue.
        type x: int
        rtype: None
        """
        self.stackNewest.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        rtype: int
        """
        if not self.stackOldest:
            while self.stackNewest:
                self.stackOldest.append(self.stackNewest.pop())

        return self.stackOldest.pop()
    
    def peek(self):
        """
        Get the front element.
        rtype: int
        """
        if not self.stackOldest:
            while self.stackNewest:
                self.stackOldest.append(self.stackNewest.pop()) 
                
        return self.stackOldest[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        rtype: bool
        """
        if not self.stackNewest and not self.stackOldest:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()