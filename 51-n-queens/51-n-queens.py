class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        ans = []
        board = []
        for i in range(n):
            board.append(['.']*n)

        def backTrack(r):
            if r==n:
                temp = ["".join(row) for row in board]
                ans.append(temp)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                else:
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    board[r][c]='Q'

                    backTrack(r+1)

                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    board[r][c]='.'

        backTrack(0)
        return ans