# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # recursive solution
    # Time complexity is O(n^n) so that very slow code.
    def reverseList(self, head: ListNode):
        if head is None or head.next is None:
            return head
        
        re_head = self.reverseList(head.next)
        tmp = re_head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = head
        head.next = None
        
        return re_head
        
    # recursive solution
    def reverseList_sol2(self, head: ListNode):
        return self.reverse(head)

    def reverse(self, node: ListNode, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n, node)

    # iterative solution
    def reverseList_sol3(self, head: ListNode):
        prev, curr = None, head
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n

        return prev

        
        
        
        
        
        
        
        