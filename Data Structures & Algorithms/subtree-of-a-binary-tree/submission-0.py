# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getString(node):
            if not node:
                return "#"
            
            return str(node.val) + getString(node.left) + getString(node.right)
        
        string1 = getString(root)
        string2 = getString(subRoot)

        return string2 in string1