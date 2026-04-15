class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # from ocean to mountain
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(a, b, visited):
            visited.add((a, b))
            for d in dirs:
                na, nb = a + d[0], b + d[1]
                if 0 <= na < m and 0 <= nb < n and (na, nb) not in visited and heights[na][nb] >= heights[a][b]:
                    dfs(na, nb, visited) 

        for i in range(n):
            dfs(0, i, pac)
            dfs(m-1, i, atl)
        for j in range(m):
            dfs(j, 0, pac)
            dfs(j, n-1, atl)
        
        res = []
        for c, d in pac.intersection(atl):
            res.append([c, d])
        return res
