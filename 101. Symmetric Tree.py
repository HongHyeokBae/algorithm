import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # my iterative solution
    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        
        res, q = True, [root]
        
        while q:
            temp = []
            for node in q:
                temp.extend([node.left, node.right])
            for i in range(len(temp)//2):
                left = temp[i].val if temp[i] else temp[i]
                right = temp[-(i+1)].val if temp[-(i+1)] else temp[-(i+1)]
                if left != right:
                    res = False
                    
            q = [node for node in temp if node]
            
        return res

    # recursive solution
    # Two trees are symmetric if:
    #   1. Both roots have same value
    #   2. The right subtree of each tree is a mirror reflection of the left subtree of the other tree
    def isSymmetric_sol2(self, root: TreeNode):
        if not root:
            return True
        return self.is_symmetric(root.left, root.right)
        
    def is_symmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            left_res = self.is_symmetric(left.left, right.right)
            right_res = self.is_symmetric(left.right, right.left)
            return left_res and right_res
        else:
            return False

    # iterative solution
    # same idea with recursive solution but using queue    
    def is_symmetric_sol3(self, root: TreeNode):
        if not root:
            return True
        
        q = collections.deque([root.left, root.right])
        while q:
            left, right = q.popleft(), q.popleft()
            if left is None and right is None:   continue
            if left is None or right is None:    return False

            if left.val == right.val:
                q.extend([left.left, right.right])
                q.extend([left.right, right.left])
            else:
                return False
            
        return True

            

    
                    
                