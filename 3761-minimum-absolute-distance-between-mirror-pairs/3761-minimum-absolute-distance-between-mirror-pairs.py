from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x: int) -> int:
            rev = 0
            while x > 0:
                rev = rev * 10 + x % 10
                x //= 10
            return rev
        
        last_pos = {}
        ans = float('inf')

        for i, x in enumerate(nums):
            if x in last_pos:
                ans = min(ans, i - last_pos[x])

            last_pos[reverse_num(x)] = i

        return -1 if ans == float('inf') else ans