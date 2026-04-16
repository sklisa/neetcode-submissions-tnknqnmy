class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        
        def find(node):
            if parent[node] == node:
                return node
            return find(parent[node])
        
        def union(a, b):
            parentA = find(a)
            parentB = find(b)

            if parentA != parentB:
                parent[parentA] = parentB
        
        for i in range(len(edges)):
            c, d = edges[i][0], edges[i][1] 
            union(c, d)
        
        res = 0
        for i in range(n):
            if parent[i] == i:
                res += 1
            
        return res