class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        r_zeros = [0] * COLS

        zero_c = []
        r_flag = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    r_flag = True
                    zero_c.append(c)
            
            if r_flag:
                matrix[r] = r_zeros
                r_flag = False

        if zero_c:
            for r in range(ROWS):
                if matrix[r][0] != 0:
                    for c in zero_c:
                            matrix[r][c] = 0
