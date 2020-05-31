

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s, t):
        """
        type s: TreeNode
        type t: TreeNode
        rtype: bool
        """
        s_ordered = self.getOrdered(s)
        t_ordered = self.getOrdered(t)
        
        return t_ordered in s_ordered
          
    def getOrdered(self, root):
        stack, visited = [root], []
        while stack:
            n = stack.pop()
            if not n:
                visited.append(None)
            else:
                visited.append(n)
                stack.append(n.right)
                stack.append(n.left)
               
        ordered = ""
        for n in visited:
            ordered += " #" + str(n.val) if n else " $"
        
        return ordered
        