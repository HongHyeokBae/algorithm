

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        type root: TreeNode
        type p: TreeNode
        type q: TreeNode
        rtype: TreeNode
        """
        parent = {root: None}
        stack = [root]

        while (p not in parent) or (q not in parent):
            node = stack.pop()
            
            if node.right and node.right not in parent:
                parent[node.right] = node
                stack.append(node.right)

            if node.left and node.left not in parent:
                parent[node.left] = node
                stack.append(node.left)
        
        ancestor = []
        while p:
            ancestor.append(p)
            p = parent[p]
          
        while q not in ancestor:
            q = parent[q]
        
        return q

    def lowestCommonAncestor_sol2(self, root, p, q):
        return self.findAncestor(root, p, q)
        
    def findAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        
        pOnLeft = self.cover(root.left, p)
        qOnLeft = self.cover(root.left, q)
        
        if pOnLeft == qOnLeft:
            if pOnLeft:
                return self.findAncestor(root.left, p, q)
            else:
                return self.findAncestor(root.right, p, q)
        
        return root
        
    def cover(self, root, node):
        if root == node:
            return True
        if not root:
            return False
        return self.cover(root.left, node) or self.cover(root.right, node)
            
        