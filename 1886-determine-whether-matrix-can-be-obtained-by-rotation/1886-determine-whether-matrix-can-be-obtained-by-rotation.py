class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90(matrix):     
            n = len(matrix)
            return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate90(mat)
        return False