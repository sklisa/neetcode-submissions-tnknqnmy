class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time O(ElogV), Space O(E+N)
        # Dijkstra
        # finding the longest path
        adj_list = defaultdict(list)
        dist = [float('inf')] * n   # find min time for each node to be reached
        dist[k-1] = 0
        for ui, vi, ti in times:
            adj_list[ui].append((vi, ti))
        heap = [(0, k)] # (time, node)
        while heap:
            time, curr = heapq.heappop(heap)
            for vi, ti in adj_list[curr]:
                if dist[vi-1] > time + ti:
                    dist[vi-1] = time + ti
                    heapq.heappush(heap, (time + ti, vi))

        if max(dist) == float('inf'):   # any of the node being unreachable
            return -1

        return max(dist)