class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(a, b):
            grid[a][b] = 0
            temp = 1
            for d in dirs:
                na, nb = a + d[0], b + d[1]
                if 0<=na<m and 0<=nb<n and grid[na][nb] == 1:
                    temp += dfs(na, nb)
            return temp
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    res = max(res, area)
            
        return res