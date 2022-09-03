class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not any(board): return False
        m, n = len(board), len(board[0])

        def dfs(x:int, y:int, i: int = 0):
            if i == len(word) - 1: return board[x][y] == word[i]
            if board[x][y] != word[i]: return False
            value = board[x][y]
            board[x][y] = '#'
            for r, c in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if 0 <= r < m and 0 <= c < n and dfs(r, c, i + 1):
                    return True
            board[x][y] = value
            return False

        return any(dfs(x, y) for x in range(m) for y in range(n))