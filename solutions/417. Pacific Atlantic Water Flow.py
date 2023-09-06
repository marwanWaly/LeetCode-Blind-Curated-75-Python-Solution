class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        alt, pac = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prev_height):
            if (r, c) in visit or r not in range(ROWS) or c not in range(COLS) or heights[r][c] < prev_height:
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])


        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, alt, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, alt, heights[ROWS - 1][c])
        
        return alt & pac
