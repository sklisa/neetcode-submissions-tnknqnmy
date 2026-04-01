# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = deque(preorder)
        def build(l, r):
            if l > r:
                return None
            val = self.preorder.popleft()
            if l == r:
                return TreeNode(val)
            idx = inorder.index(val)
            node = TreeNode(val)
            node.left = build(l, idx-1)
            node.right = build(idx+1, r)
            return node
        
        return build(0, len(preorder)-1)