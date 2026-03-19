class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        px = [[0] * cols for _ in range(rows)]
        py = [[0] * cols for _ in range(rows)]
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                px[i][j] = (1 if grid[i][j] == 'X' else 0)
                py[i][j] = (1 if grid[i][j] == 'Y' else 0)
                
                if i > 0:
                    px[i][j] += px[i-1][j]
                    py[i][j] += py[i-1][j]
                if j > 0:
                    px[i][j] += px[i][j-1]
                    py[i][j] += py[i][j-1]
                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]
                    py[i][j] -= py[i-1][j-1]
                
                if px[i][j] > 0 and px[i][j] == py[i][j]:
                    count += 1
        
        return count