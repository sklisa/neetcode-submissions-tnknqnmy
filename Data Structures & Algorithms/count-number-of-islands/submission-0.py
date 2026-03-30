class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time O(MN), Space O(MN)
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def dfs(a, b):
            grid[a][b] = '0'
            for d in dirs:
                na, nb = a + d[0], b + d[1]
                if 0 <= na < m and 0 <= nb < n and grid[na][nb] == '1':
                    dfs(na, nb)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res