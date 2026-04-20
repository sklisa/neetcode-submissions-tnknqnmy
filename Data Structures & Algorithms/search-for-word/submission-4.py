class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time O(N^2M^2)
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def dfs(a, b, ind):
            if ind == len(word)-1:
                return True
            
            board[a][b] = '#'
            
            for d in dirs:
                na, nb = a+d[0], b+d[1]
                if 0 <= na < m and 0 <= nb < n and board[na][nb] == word[ind+1]:
                    if dfs(na, nb, ind+1):
                        return True
            board[a][b] = word[ind]
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
