class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        root = TrieNode()
        for w in words:
            root.add_word(w)

        def dfs(r, c, node, word):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] not in node.children or (r, c) in visited:
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)

            for x, y in directions:
                dfs(r + x, c + y, node, word)
    
            visited.remove((r, c))
        
       
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res) 
