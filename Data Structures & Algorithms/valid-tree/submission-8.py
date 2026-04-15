class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time O(N), Space O(N)
        # Union find
        # process each edge; if two nodes already belongs to one parent, there is cycle
        parent = [i for i in range(n)]

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
        
        for i, j in edges:
            if not union(i, j):
                return False
        
        numGroups = 0
        for i in range(n):
            if parent[i] == i:
                numGroups += 1
        
        return numGroups == 1