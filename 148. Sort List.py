# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode):
        if not head or not head.next:
            return head
        
        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        right = self.sortList(prev.next)
        prev.next = None
        left = self.sortList(head)
        
        return self.merge(left, right)

    def merge(self, left, right):
        head = None
        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next
        temp = head
        
        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        
        if left:
            temp.next = left
        else:
            temp.next = right

        return head

            
        
