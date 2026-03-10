class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j][k] = number of stable arrays with i zeros and j ones ending with digit k (0 or 1)
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        # Base cases: arrays consisting of only zeros or only ones
        for i in range(1, min(limit, zero) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp[0][j][1] = 1

        # Fill the DP table for i>0 and j>0
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Append 0 to a sequence ending with either digit
                val0 = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                # Subtract sequences that would create a run of limit+1 zeros
                if i > limit:
                    val0 = (val0 - dp[i - limit - 1][j][1]) % MOD
                dp[i][j][0] = val0

                # Append 1 to a sequence ending with either digit
                val1 = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                # Subtract sequences that would create a run of limit+1 ones
                if j > limit:
                    val1 = (val1 - dp[i][j - limit - 1][0]) % MOD
                dp[i][j][1] = val1

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD