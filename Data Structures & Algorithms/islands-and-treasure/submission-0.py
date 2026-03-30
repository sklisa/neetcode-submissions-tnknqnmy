class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS
        # starts from all treasures at the same time
        # add to queue by layer to keep track of distance
        # do not add if water
        q = deque()
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647
        dist = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            layerlength = len(q)
            for i in range(layerlength):
                a, b = q.popleft()
                for d in dirs:
                    na, nb = a + d[0], b + d[1]
                    if 0<=na<m and 0<=nb<n and grid[na][nb] == INF:
                        grid[na][nb] = dist
                        q.append((na, nb))
            dist += 1
        