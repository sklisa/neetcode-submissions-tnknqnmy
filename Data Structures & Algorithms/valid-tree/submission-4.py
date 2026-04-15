class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time O(N), Space O(N)
        # Cycle detection, DFS
        if len(edges) == 0:
            return True

        neighbors = defaultdict(set)
        for a, b in edges:
            if a == b:
                return False
            neighbors[a].add(b)
            neighbors[b].add(a)
        
        res = True
        visited = set([0])
        def dfs(parent, curr):
            nonlocal res
            nonlocal visited
            visited.add(curr)
            for nb in neighbors[curr]:
                if nb != parent:
                    if nb in visited:
                        res = False
                        return
                    dfs(curr, nb)

        for i in neighbors[0]:
            dfs(0, i)
        
        return res if len(visited) == n else False
        