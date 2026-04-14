from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            
            if j == m:
                return float('inf')

            ans = dp(i, j + 1)

            pos, limit = factory[j]
            dist = 0

            for k in range(1, limit + 1):
                if i + k > n:
                    break

                dist += abs(robot[i + k - 1] - pos)
                ans = min(ans, dist + dp(i + k, j + 1))

            return ans

        return dp(0, 0)