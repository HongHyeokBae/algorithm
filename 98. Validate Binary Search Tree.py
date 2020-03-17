# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Inorder traversal
    def isValidBST(self, root: TreeNode) -> bool:
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