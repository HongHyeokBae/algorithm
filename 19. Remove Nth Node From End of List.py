

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        type head: ListNode
        type n: int
        rtype: ListNode
        """
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1
        
        # curr: node before the n-th node
        i, curr = 0, head
        while i < (length - n - 1):
            curr = curr.next
            i += 1
            
        # remove head
        if n == length:
            return head.next
        else:
            curr.next = curr.next.next
        
        return head

    def removeNthFromEnd_sol2(self, head, n):
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        # move curr to n node
        for _ in range(n):
            curr = curr.next
        
        # if curr hits the end,
        # prev will be (length-n) node before.
        while curr:
            prev, curr = prev.next, curr.next
        prev.next = prev.next.next
        return dummy.next