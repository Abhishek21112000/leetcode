from typing import List
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        NEG_INF = float("-inf")

       
        dp = [[[NEG_INF] * (k + 1) for _ in range(n)] for _ in range(m)]

        val = grid[0][0]
        cost = 0 if val == 0 else 1
        score = val  # 0, 1, or 2

        if cost <= k:
            dp[0][0][cost] = score

        # Fill DP
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                c_add = 0 if val == 0 else 1
                s_add = val  

                for c in range(k + 1):
                    if i == 0 and j == 0:
                        continue  
                    best = NEG_INF
                
                    if i > 0 and dp[i - 1][j][c] != NEG_INF:
                        best = max(best, dp[i - 1][j][c])
                    if j > 0 and dp[i][j - 1][c] != NEG_INF:
                        best = max(best, dp[i][j - 1][c])

                    if best != NEG_INF:
                        new_c = c + c_add
                        if new_c <= k:
                            dp[i][j][new_c] = max(dp[i][j][new_c], best + s_add)

        ans = max(dp[m - 1][n - 1])
        return ans if ans != NEG_INF else -1
