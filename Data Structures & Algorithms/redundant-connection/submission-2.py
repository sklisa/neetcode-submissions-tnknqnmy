class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = set()
        cycleStart = -1
        cycle = set()

        def dfs(curr, parent):
            nonlocal cycleStart
            if curr in visited:
                cycleStart = curr
                return True
            visited.add(curr)

            for nb in adj_list[curr]:
                if nb == parent:
                    continue
                if dfs(nb, curr):
                    if cycleStart != -1:
                        cycle.add(curr)
                    if cycleStart == curr:
                        cycleStart = -1
                    return True
            return False

        dfs(1, 0)
        for i in range(len(edges)-1, -1, -1):
            a, b = edges[i]
            if a in cycle and b in cycle:
                return [a, b]
        return []
        