from collections import defaultdict
from bisect import bisect_left

class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)
        mp = defaultdict(list)

        for i, v in enumerate(nums):
            mp[v].append(i)

        res = []

        for q in queries:
            arr = mp[nums[q]]

            if len(arr) == 1:
                res.append(-1)
                continue

            i = bisect_left(arr, q)

            prev = arr[i - 1]
            nxt = arr[(i + 1) % len(arr)]

            d1 = min(abs(q - prev), n - abs(q - prev))
            d2 = min(abs(q - nxt), n - abs(q - nxt))

            res.append(min(d1, d2))

        return res