from collections import Counter
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:

        n = len(nums) - 1
        freq = Counter(nums)

        if freq[n] != 2:
            return False

        for i in range(1, n):
            if freq[i] != 1:
                return False

        return True