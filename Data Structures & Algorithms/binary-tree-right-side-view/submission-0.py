# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            currlen = len(q)
            for i in range(currlen):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i == currlen-1:
                    res.append(curr.val)
        return res