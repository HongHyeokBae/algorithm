

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, sum):
        """
        type root: TreeNode
        type sum: int
        rtype: int
        """
        return self.findPath(root, [], sum)
        
    def findPath(self, node, paths, sum):
        if not node:
            return 0
        
        paths = [node.val + path for path in paths]
        paths.append(node.val)
        count = paths.count(sum)
        
        return count + self.findPath(node.left, paths, sum) + self.findPath(node.right, paths, sum)

    def pathSum_sol2(self, root, sum):
        return self.find(root, sum, 0, {0:1})

    def find(self, node, target, currSum, pathCount):
        if not node:
            return 0
        
        currSum += node.val
        oldPathSum = currSum - target
        counts = pathCount.get(oldPathSum, 0)
        
        if currSum == target:
            counts += 1
        
        pathCount[currSum] = pathCount.get(currSum, 0) + 1
        counts += self.find(node.left, target, currSum, pathCount)
        counts += self.find(node.right, target, currSum, pathCount)
        pathCount[currSum] -= 1

        return counts

        
        
        
        