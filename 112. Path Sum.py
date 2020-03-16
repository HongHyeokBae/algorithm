# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = False
        
    def hasPathSum(self, root: TreeNode, sum: int):
        if not root:
            return False
        
        self.pathSum(root, 0, sum)
        return self.res
    
    def pathSum(self, root, pathSum, sum):
        if not root:
            return
        
        pathSum += root.val
        if not root.left and not root.right:
            if sum == pathSum:
                self.res = True
            return
        else:
            self.pathSum(root.left, pathSum, sum)
            self.pathSum(root.right, pathSum, sum)

    def hasPathSum_sol2(self, root: TreeNode, sum: int):
        if not root:
            return False
        if root.left == None and root.right == None and sum - root.val == 0:
            return True
        
        sum -= root.val
        return self.hasPathSum_sol2(root.left, sum) or self.hasPathSum_sol2(root.right, sum)
        
        
            
            