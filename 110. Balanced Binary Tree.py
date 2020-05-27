

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        type root: TreeNode
        rtype: bool
        """         
        def getHeight(root):
            if not root:
                return 0

            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)            
            if rightHeight == -99 or leftHeight == -99:
                return -99
            
            if abs(leftHeight - rightHeight) > 1:
                return -99
            return max(leftHeight, rightHeight) + 1
        
        return getHeight(root) != -99        