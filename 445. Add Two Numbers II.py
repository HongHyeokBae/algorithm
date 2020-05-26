

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # reverse l1, l2
    def addTwoNumbers(self, l1, l2):
        """
        type l1: ListNode
        type l2: ListNode
        rtype: ListNode
        """
        rev_l1 = self.reverseList(l1)
        rev_l2 = self.reverseList(l2)

        carry = 0
        res = temp = ListNode(0)
        while rev_l1 or rev_l2 or carry:
            n1 = n2 = 0
            if rev_l1:
                n1 = rev_l1.val
                rev_l1 = rev_l1.next
            if rev_l2:
                n2 = rev_l2.val
                rev_l2 = rev_l2.next
                
            carry, n = divmod(n1+n2+carry, 10)
            temp.next = ListNode(n)
            temp = temp.next
            
        res = self.reverseList(res.next)
        
        return res
        
    def reverseList(self, head):
        nodeArr = []
        revHead = temp = ListNode(0)
        while head:
            nodeArr.append(head)
            head = head.next
        
        for i in range(len(nodeArr)-1, -1, -1):
            temp.next = nodeArr[i]
            temp = temp.next
        temp.next = None
               
        return revHead.next

        # 1. get length of l1, l2
        # 2. add zeros to the front of shorter list
        # 3. add values recursively
    
    def addTwoNumbers_sol2(self, l1, l2):
        len1 = self.getLength(l1)
        len2 = self.getLength(l2)
        if len1 > len2:
            l2 = self.padZero(len1 - len2, l2)
        else:
            l1 = self.padZero(len2 - len1, l1)
            
        carry, head = self.addLists(l1, l2)
        if carry:
            temp = ListNode(1)
            temp.next = head
            head = temp
            
        return head
        
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def padZero(self, length, head):
        for i in range(length):
            temp = ListNode(0)
            temp.next = head
            head = temp
        return head
    
    def addLists(self, l1, l2):
        if not l1 and not l2:
            return (0, None)
        carry, prev = self.addLists(l1.next, l2.next)
        n1 = l1.val
        n2 = l2.val
        carry, n = divmod(n1+n2+carry, 10)
        curr = ListNode(n)
        curr.next = prev
        return (carry, curr)

    # push value of l1, l2 to stack
    def addTwoNumbers_sol3(self, l1, l2):
        s1, s2 = [], []
        while l1 or l2:
            if l1:  s1.append(l1.val)
            if l2:  s2.append(l2.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        carry = 0
        head = ListNode(0)
        while s1 or s2 or carry:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0
            carry, n = divmod(n1+n2+carry, 10)
            temp = ListNode(n)
            temp.next = head
            head = temp
        
        temp = head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        
        return head
            