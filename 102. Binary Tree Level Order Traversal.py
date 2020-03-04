from typing import List


# Tree, Breadth-first Search
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, res = [(root, 0)], []
        cur_level = 0
        level_res = []
        if root == None:
            return res
        
        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            
            if cur_level == level:
                level_res.append(node.val)
            else:
                res.append(level_res)
                level_res = [node.val]
                cur_level = level
        
        res.append(level_res)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level = [], [root]
        
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        
        return res

        