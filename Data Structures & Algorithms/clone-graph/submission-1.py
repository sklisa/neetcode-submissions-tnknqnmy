"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        if not node:
            return None
        copydict = dict()
        
        def dfs(curr):
            if curr.val in copydict:
                return copydict[curr.val]
            copy = Node(curr.val, [])
            copydict[curr.val] = copy
            for n in curr.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node)