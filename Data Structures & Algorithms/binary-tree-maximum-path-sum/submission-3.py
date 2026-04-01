# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(node):
            if not node:
                return 0
            
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)
            currsum = node.val + leftmax + rightmax 
            self.res = max(self.res, node.val, currsum, node.val + max(rightmax, leftmax))
            return max(node.val, node.val + max(rightmax, leftmax))
        
        dfs(root)
        return self.res