class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time O(N), Space O(N)
        # Cycle detection, DFS
        if len(edges) > (n-1):
            return False

        neighbors = defaultdict(set)
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)

        visited = set()
        def dfs(parent, curr):
            visited.add(curr)
            for nb in neighbors[curr]:
                if nb != parent:
                    if nb in visited:
                        return False
                    if not dfs(curr, nb):
                        return False
            return True
        
        
        return dfs(-1, 0) and len(visited) == n
        