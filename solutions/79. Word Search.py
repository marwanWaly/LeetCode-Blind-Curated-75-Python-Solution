class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS= len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r not in range(ROWS) or c not in range(COLS) or (r, c) in path or board[r][c] != word[i]:
                return False

            path.add((r, c))

            for d1, d2 in directions:
                if dfs(r + d1, c + d2, i + 1): return True
            
            path.remove((r, c))

            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True

        return False
