class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n, m = len(mat) , len(mat[0])
        for row_idx, row in enumerate(mat):
            shift = k % m
            if shift == 0:
                continue
            if row_idx % 2 == 0:
                shifted = row[shift:] + row[:shift]
            else:
                shifted = row[-shift:] + row[:-shift]
            if shifted != row:
                return False
        return True