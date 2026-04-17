class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Time O(NLogN), Space O(N^2)
        # Dijkstra
        m, n = len(grid), len(grid[0])
        total = [[float('inf')] * n for _ in range(m)]
        heap = [(grid[0][0], 0, 0)] # time, i, j
        dirs = [(0, 1), (0, -1,), (1, 0), (-1, 0)]

        while heap:
            time, i, j = heapq.heappop(heap)
            for d in dirs:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and max(time, grid[ni][nj]) < total[ni][nj]:
                    heapq.heappush(heap, (max(time, grid[ni][nj]), ni, nj))
                    total[ni][nj] = max(time, grid[ni][nj])
            
        return total[m-1][n-1]

