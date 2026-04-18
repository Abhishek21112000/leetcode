class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev_num = int(str(n)[::-1])
        return abs(n - rev_num)