# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Inorder traversal
    def isValidBST(self, root):
        """
        type root: TreeNode
        rtype: bool
        """
        res, stack = True, []
        node, prev = root, None
        
        while stack or node:    
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                
                if prev is None:
                    prev = node.val
                else:
                    if prev >= node.val:
                        return False
                    prev = node.val
                
                node = node.right
                
        return res

    def isValidBST_sol2(self, root):
        return self.checkBST(root, None, None)

    def checkBST(self, node, minVal, maxVal):
        if not node:
            return True

        if (minVal != None and node.val < minVal) or (maxVal != None and node.val > maxVal):
            return False
        
        if not self.checkBST(node.left, minVal, node.val) or not self.checkBST(node.right, node.val, maxVal):
            return False
        
        return True