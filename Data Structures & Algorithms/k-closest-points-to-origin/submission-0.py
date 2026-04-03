class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in range(len(points)):
            dist = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush(heap, (dist, i))
        
        for _ in range(k):
            _, ind = heapq.heappop(heap)
            res.append(points[ind])
        return res