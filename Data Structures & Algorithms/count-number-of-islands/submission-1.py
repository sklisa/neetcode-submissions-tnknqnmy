class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time O(MN), Space O(MN)
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def bfs(a, b):
            q = deque()
            grid[a][b] = '0'
            q.append((a, b))

            while q:
                r, c = q.popleft()
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        q.append((nr, nc))
                        grid[nr][nc] = '0'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)
        
        return res