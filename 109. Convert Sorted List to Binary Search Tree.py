

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        """
        type head: ListNode
        rtype: TreeNode
        """
        toArr = []
        while head:
            toArr.append(head.val)
            head = head.next
        
        def convertListToBST(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            node = TreeNode(toArr[mid])
            if l == r:
                return node
            
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
        
            return node
    
        root = convertListToBST(0, len(toArr) - 1)
        
        return root
        
    def recur(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.recur(nums[:mid])
        node.right = self.recur(nums[mid+1:])
        
        return node

