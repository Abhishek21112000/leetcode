from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        arr = sorted(zip(robots, distance))
        walls.sort()
        n = len(arr)
        W = walls

        dp = [0, 0]

        for i in range(n):
            pos, dist = arr[i]
            new_dp = [0, 0]

            for j in range(2):
                left = pos - dist
                if i > 0:
                    left = max(left, arr[i-1][0] + 1)
                lc = bisect_left(W, left)
                rc = bisect_right(W, pos)
                optA = dp[0] + (rc - lc)

                right = pos + dist
                if i + 1 < n:
                    if j == 0:
                        right = min(right, arr[i+1][0] - arr[i+1][1] - 1)
                    else:
                        right = min(right, arr[i+1][0] - 1)
                lc = bisect_left(W, pos)
                rc = bisect_right(W, right)
                optB = dp[1] + (rc - lc)

                new_dp[j] = max(optA, optB)

            dp = new_dp

        return dp[1]