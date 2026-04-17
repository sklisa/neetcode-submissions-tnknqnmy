class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Dikjstra
        if k > len(flights)-2:
            return -1
        adjlist = defaultdict(list)
        for fr, to, pr in flights:
            adjlist[fr].append((to, pr))
        
        heap = [(0, src, -1)]    # cost, place, stops
        dist = [[float('inf')] * len(flights) for _ in range(len(flights))] # cost

        while heap:
            cost, curr, stops = heapq.heappop(heap)
            for nb, pr in adjlist[curr]:
                if stops < k and cost + pr < dist[nb][stops+1]:
                    dist[nb][stops+1] = cost + pr
                    heapq.heappush(heap, (cost + pr, nb, stops+1))

        res = float('inf')
        for i in range(k+1):
            res = min(res, dist[dst][i])
        
        if res == float('inf'):
            return -1
        
        return res
