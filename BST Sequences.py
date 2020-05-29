

class Solution:
    def BSTSequences(self, root):
        return self.recur(root)

    def recur(self, root):
        if not root.left and not root.right:
            return [[root.val]]

        left = self.recur(root.left)
        right = self.recur(root.right)

        outputs = []
        for l in left:
            for r in right:
                outputs.append([root.val] + l + r)
                outputs.append([root.val] + r + l)

        return outputs

                        