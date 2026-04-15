class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time O(EV), Space O(N)
        # Bellman Ford
        # finding the shortest path
        dist = [float('inf')] * n   # find min time for each node to be reached
        dist[k-1] = 0
        for i in range(n-1):
            for ui, vi, ti in times:
                if dist[ui-1] + ti < dist[vi-1]:
                    dist[vi-1] = dist[ui-1] + ti

        if max(dist) == float('inf'):
            return -1

        return max(dist) 