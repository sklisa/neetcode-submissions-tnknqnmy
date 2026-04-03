class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time O(nlogk), Space O(k)
        heap = []
        res = []
        for i in range(len(points)):
            dist = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush(heap, (-1 * dist, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for h in heap:
            res.append(points[h[1]])
        return res