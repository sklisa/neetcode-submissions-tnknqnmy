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
            copy = Node(curr.val, [])
            copydict[curr.val] = copy
            for n in curr.neighbors:
                if n.val in copydict:
                    copyn = copydict[n.val]
                else:
                    copyn = dfs(n)
                copy.neighbors.append(copyn)
            return copy
        
        return dfs(node)