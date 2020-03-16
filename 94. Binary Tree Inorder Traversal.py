from typing import List


# Stack, Hash Table, Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
#     recursive solution
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
            
        
    def inorderTraversal(self, root: TreeNode):
        res = []
        self.inorder(root, res)
        
        return res

#   iterative solution    
    def inorderTraversal_sol2(self, root: TreeNode):
        s, res = [], []
        node = root
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                res.append(node.val)
                node = node.right
            
        return res
                
        