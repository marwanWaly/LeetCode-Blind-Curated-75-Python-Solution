class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = []
        visited = [[0 for c in range(COLS)] for r in range(ROWS)]

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = 0, 0
        curr_dir = 0
        while True:
            res.append(matrix[r][c])
            visited[r][c] = 1

            new_r = r + direction[curr_dir][0]
            new_c = c + direction[curr_dir][1]
            if new_r in range(ROWS) and new_c in range(COLS) and visited[new_r][new_c] == 0:
                r, c = new_r, new_c
            else:
                curr_dir = (curr_dir + 1) % len(direction)
                new_r = r + direction[curr_dir][0]
                new_c = c + direction[curr_dir][1]
                if new_r in range(ROWS) and new_c in range(COLS) and visited[new_r][new_c] == 0:
                    r, c = new_r, new_c
                else:
                    break
        
        return res
