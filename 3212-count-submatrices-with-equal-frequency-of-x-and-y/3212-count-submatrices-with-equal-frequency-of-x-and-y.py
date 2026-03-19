class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        px = [0] * (cols + 1)
        py = [0] * (cols + 1)
        
        count = 0
        for row in grid:
            new_px = [0] * (cols + 1)
            new_py = [0] * (cols + 1)
            for j, cell in enumerate(row):
                new_px[j+1] = new_px[j] + px[j+1] - px[j] + (cell == 'X')
                new_py[j+1] = new_py[j] + py[j+1] - py[j] + (cell == 'Y')
                if new_px[j+1] > 0 and new_px[j+1] == new_py[j+1]:
                    count += 1
            px, py = new_px, new_py
        
        return count