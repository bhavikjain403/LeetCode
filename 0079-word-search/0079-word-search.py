class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        h, w = len(board), len(board[0])
        
        def dfs_search(idx, x, y):
            if x < 0 or x == w or y < 0 or y == h or word[idx] != board[y][x]:
                return False
            if idx == len(word) - 1:
                return True
            cur = board[y][x]
            board[y][x] = '#'
            found = dfs_search(idx + 1, x + 1, y) or dfs_search(idx + 1, x - 1, y) or dfs_search(idx + 1, x, y + 1) or dfs_search(idx + 1, x, y - 1)
            board[y][x] = cur
            return found
        
        return any(dfs_search(0, x, y) for y in range(h) for x in range(w))   