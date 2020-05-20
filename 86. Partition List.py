

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):
        """
        type head: ListNode
        type x: int
        rtype: ListNode
        """
        curr = head
        less, greater = ListNode(0), ListNode(0)
        less_head, greater_head = less, greater
        
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        
        greater.next = None
        
        less.next = greater_head.next
        return less_head.next