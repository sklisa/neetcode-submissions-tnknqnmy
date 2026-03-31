# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0

        def dfs(node, currmax):
            if not node:
                return
            if node.val >= currmax:
                self.count += 1
            dfs(node.left, max(currmax, node.val))
            dfs(node.right, max(currmax, node.val))

        dfs(root, float('-inf'))
        return self.count
