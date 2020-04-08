# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        head, temp = dummy, dummy
        extra = 0
        while l1 or l2:
            n1, n2 = 0, 0
            if l1:  
                n1 = l1.val
                l1 = l1.next
            if l2:  
                n2 = l2.val
                l2 = l2.next
            
            digit = n1 + n2 + extra
            if digit >= 10:
                digit = digit - 10
                extra = 1
            else:
                extra = 0
            temp.next = ListNode(digit)
            temp = temp.next
        if extra == 1:
            temp.next = ListNode(1)
        
        return head.next

    # cleaner code
    def addTwoNumbers_sol2(self, l1, l2):
        head = temp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            n1 = n2 = 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next
            carry, val = divmod(n1 + n2 + carry, 10)
            temp.next = ListNode(val)
            temp = temp.next

        return head.next