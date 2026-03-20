from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m , n = len(grid), len(grid[0])
        rows, cols = m - k + 1 , n - k + 1
        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                vals = []
                for r in range(i, i + k):
                    for c in range(j , j + k):
                        vals.append(grid[r][c])
                vals.sort()
                min_diff = float('inf')
                for x in range(1, len(vals)):
                    if vals[x] !=  vals[x-1]:
                        min_diff = min(min_diff, vals[x] - vals[x-1])

                ans[i][j] = 0 if min_diff == float('inf') else min_diff
        return ans


