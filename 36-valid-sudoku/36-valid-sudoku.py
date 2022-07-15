class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            d = dict()
            for j in range(9):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        for i in range(9):
            d = dict()
            for j in range(9):
                if board[j][i]!="." and board[j][i] in d.keys():
                    return False
                else:
                    d[board[j][i]]=1
        d = dict()
        for i in range(3):
            for j in range(3):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(3):
            for j in range(3,6):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(3):
            for j in range(6,9):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(3,6):
            for j in range(3):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(6,9):
            for j in range(3):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        d = dict()
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j]!="." and board[i][j] in d.keys():
                    return False
                else:
                    d[board[i][j]]=1
        return True