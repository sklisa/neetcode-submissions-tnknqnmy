class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(a, b):
            board[a][b] = 'o'
            for d in dirs:
                na, nb = a + d[0], b + d[1]
                if 0 <= na < m and 0 <= nb < n and board[na][nb] == 'O':
                    dfs(na, nb)
        
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'o':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        