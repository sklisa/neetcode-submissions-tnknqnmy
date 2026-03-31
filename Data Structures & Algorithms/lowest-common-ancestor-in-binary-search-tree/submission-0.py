# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == p.val:
                return node
            if node.val == q.val:
                return node

            if left and right:
                return node

            return left or right
            
        return dfs(root)