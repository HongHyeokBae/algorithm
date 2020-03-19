from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        root_idx = inorder.index(root.val)
        
        root.right = self.buildTree(inorder[root_idx+1:], postorder)
        root.left = self.buildTree(inorder[:root_idx], postorder)
        
        return root
        
    # The above solution takes extra spaces when function is called recursively
    def buildTree_sol2(self, inorder: List[int], postorder: List[int]):
        map_inorder = {}

        # doesn't need to find index of the root for every function call
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        global p_idx
        p_idx = len(postorder) - 1
        def recur(low, high):
            if low > high:  return None
            # using pop could make it hard to track down bug
            global p_idx
            node = TreeNode(postorder[p_idx])
            p_idx -= 1
            mid = map_inorder[node.val]
            node.right = recur(mid+1, high)
            node.left = recur(low, mid-1)
            return node
        
        return recur(0, len(inorder) - 1)
