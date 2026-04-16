from collections import defaultdict
from bisect import bisect_left
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # Store indices of each value
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = []

        for q in queries:
            arr = pos[nums[q]]

            # only one occurrence
            if len(arr) == 1:
                ans.append(-1)
                continue

            k = bisect_left(arr, q)

            # previous and next occurrence in circular manner
            prev_idx = arr[k - 1]
            next_idx = arr[(k + 1) % len(arr)] if arr[k] == q else arr[k % len(arr)]

            d1 = abs(q - prev_idx)
            d1 = min(d1, n - d1)

            d2 = abs(q - next_idx)
            d2 = min(d2, n - d2)

            ans.append(min(d1, d2))

        return ans