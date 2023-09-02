class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for c in range(m+1)] for r in range(n+1)]
        
        dp[n-1][m-1] = 1
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if not (r == n - 1 and c == m - 1):
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]
