# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preorder
        q = deque()
        self.string = ""
        def dfs(node):
            if not node:
                self.string += "#,"
                return
            self.string += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = deque(data.split(","))
        print(data)
        def dfs():
            val = q.popleft()
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
