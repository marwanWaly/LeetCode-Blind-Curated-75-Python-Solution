class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        # def dfs(r, c):
        #     if r not in range(ROWS) or c not in range(COLS) or grid[r][c] != "1":
        #         return
            
        #     grid[r][c] = '-1'
        #     dfs(r + 1, c)
        #     dfs(r - 1, c)
        #     dfs(r, c + 1)
        #     dfs(r, c - 1)

        #     return grid
        
        def bfs(i, j): # No need for visited just update the grid
            q = []
            q.append((i, j))
            while q:
                currRow, currCol = q.pop(0)
                for dr, dc in directions:
                    r = currRow + dr
                    c = currCol + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1':
                        grid[r][c] = '-1'
                        q.append((r, c))
            return grid 

        num_of_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": 
                    num_of_islands += 1
                    # dfs(r, c)
                    bfs(r, c)
        return num_of_islands
