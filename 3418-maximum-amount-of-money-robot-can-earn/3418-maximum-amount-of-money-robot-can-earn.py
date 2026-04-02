class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG = float('-inf')

        dp = [[[NEG] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for k in range(3):
                    best = NEG
                    if i > 0 and dp[i-1][j][k] != NEG:
                        best = max(best, dp[i-1][j][k])
                    if j > 0 and dp[i][j-1][k] != NEG:
                        best = max(best, dp[i][j-1][k])

                    if best != NEG:
                        dp[i][j][k] = max(dp[i][j][k], best + coins[i][j])

                    if coins[i][j] < 0 and k > 0:
                        best_neutral = NEG
                        if i > 0 and dp[i-1][j][k-1] != NEG:
                            best_neutral = max(best_neutral, dp[i-1][j][k-1])
                        if j > 0 and dp[i][j-1][k-1] != NEG:
                            best_neutral = max(best_neutral, dp[i][j-1][k-1])
                        if best_neutral != NEG:
                            dp[i][j][k] = max(dp[i][j][k], best_neutral)

        return max(dp[m-1][n-1])