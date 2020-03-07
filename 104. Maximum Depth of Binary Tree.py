# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = 0
    
    def maximum_depth(self, root, depth):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            self.res = max(self.res, depth)
        self.maximum_depth(root.left, depth + 1)
        self.maximum_depth(root.right, depth + 1)
    
    # top-down solution
    def maxDepth_sol1(self, root: TreeNode) -> int:
        self.maximum_depth(root, 1)
        
        return self.res
    
    # bottom-up solution
    def maxDepth_sol2(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth_sol2(root.left), self.maxDepth_sol2(root.right)) + 1

    # iterative solution
    # breadth-first search 
    def maxDepth_sol3(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res, q = 0, [root]
        while q:
            res += 1
            temp = []
            for node in q:
                temp.extend([node.left, node.right])
            q = [node for node in temp if node]
        
        return res