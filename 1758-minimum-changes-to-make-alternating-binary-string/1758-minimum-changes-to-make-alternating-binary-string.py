class Solution:
    def minOperations(self, s: str) -> int:
        start_0 = 0
        for i, char in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if char != expected:
                start_0 += 1
        start_1 = len(s) - start_0
        return min(start_0, start_1)
        