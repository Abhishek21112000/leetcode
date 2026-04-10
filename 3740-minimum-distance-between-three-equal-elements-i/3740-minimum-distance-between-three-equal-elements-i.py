from collections import defaultdict
from math import inf
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        g  = defaultdict(list)
        for i , x in enumerate(nums):
            g[x].append(i)

        ans = inf
        for indices in g.values():
            for h in range(len(indices) - 2):
                i, k = indices[h], indices[h + 2]
                ans = min(ans, (k - i) * 2)
        return -1 if ans == inf else ans