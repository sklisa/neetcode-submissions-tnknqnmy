class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time O(N^2logN), Space O(N^2)
        # Kruskal's
        # Union Find
        heap = [] # (dist, p1, p2)

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                dist = abs(xi-xj) + abs(yi-yj)
                heapq.heappush(heap, (dist, i, j))

        parent = [i for i in range(len(points))]

        def find(node):
            if parent[node] == node:
                return node
            return find(parent[node])
        
        def union(a, b):
            parentA = find(a)
            parentB = find(b)

            if parentA == parentB:
                return False
            
            parent[parentA] = parentB
            return True

        edges = 0
        res = 0
        while edges < len(points)-1:
            dist, i, j = heapq.heappop(heap)
            if union(i, j):
                edges += 1
                res += dist

        return res    


        