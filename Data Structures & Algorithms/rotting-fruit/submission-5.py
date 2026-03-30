class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        q = deque()
        res = 0
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        freshtotal = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshtotal += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        while q and freshtotal > 0:
            currlen = len(q)
            for _ in range(currlen):
                a, b = q.popleft()
                for d in dirs:
                    ca, cb = a + d[0], b + d[1]
                    if 0<=ca<m and 0<=cb<n and grid[ca][cb] == 1:
                        grid[ca][cb] = 2
                        q.append((ca, cb))
                        freshtotal -= 1
            res += 1
        
        if freshtotal == 0:
            return res
        else:
            return -1
