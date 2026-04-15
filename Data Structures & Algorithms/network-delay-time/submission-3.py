class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time O(E+V), Space O(E+V)
        # Shortest path faster
        # finding the shortest path
        adj_list = defaultdict(list)
        for ui, vi, ti in times:
           adj_list[ui].append((vi, ti))
        dist = [float('inf')] * n   # find min time for each node to be reached
        dist[k-1] = 0
        q = deque([k])
        while q:
            node = q.popleft()
            for nb, ti in adj_list[node]:
                if dist[node-1] + ti < dist[nb-1]:
                    dist[nb-1] = dist[node-1] + ti
                    q.append(nb)
        
        if max(dist) == float('inf'):
            return -1

        return max(dist)