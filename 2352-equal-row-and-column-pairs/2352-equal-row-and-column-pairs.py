from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)

        result = 0
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            result += row_count[col_tuple]

        return result

        