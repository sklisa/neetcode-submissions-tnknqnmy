class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0 -> 0, 0
        # 1 -> 0, 1
        # 2 -> 0, 2
        # 3 -> 1, 0
        # 4 -> 1, 1
        # 5 -> 1, 2

        def check():
            for i in range(len(board)):
                if not checkrow(i) or not checkcol(i) or not checkgrid(i//3, i%3):
                    return False
            return True
        
        def checkrow(r):
            seen = set()
            for char in board[r]:
                if char == ".":
                    continue
                elif char in seen:
                    return False
                else:
                    seen.add(char)
            return True
        
        def checkcol(c):
            seen = set()
            for i in range(len(board)):
                char = board[i][c]
                if char == ".":
                    continue
                elif char in seen:
                    return False
                else:
                    seen.add(char)
            return True
        
        def checkgrid(p, q):
            seen = set()
            for row in range(p*3, p*3+3):
                for col in range(q*3, q*3+3):
                    char = board[row][col]
                    if char == ".":
                        continue
                    elif char in seen:
                        return False
                    else:
                        seen.add(char)
            return True

        return check()

