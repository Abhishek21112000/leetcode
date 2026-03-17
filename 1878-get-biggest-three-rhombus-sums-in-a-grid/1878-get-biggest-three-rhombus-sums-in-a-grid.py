from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        top3 = set()

        def add(val):
            top3.add(val)
            if len(top3) > 3:
                top3.discard(min(top3))  
        for r in range(m):
            for c in range(n):
                add(grid[r][c])
                k = 1
                while (r - k >= 0 and r + k < m and
                       c - k >= 0 and c + k < n):
                    total = 0
                    for d in range(k):
                        total += grid[r - k + d][c + d]   
                        total += grid[r + d][c + k - d]  
                        total += grid[r + k - d][c - d]  
                        total += grid[r - d][c - k + d]   
                    add(total)
                    k += 1

        return sorted(top3, reverse=True)