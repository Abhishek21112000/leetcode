from math import isqrt
from functools import reduce
from operator import xor

class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = max(1, isqrt(n))

        diff = {}

        for l, r, k, v in queries:
            if k > B:
                for idx in range(l, r + 1, k):
                    nums[idx] = nums[idx] * v % MOD
            else:
                res = l % k
                key = (k, res)
                if key not in diff:
                    seq_len = (n - 1 - res) // k + 1 if res < n else 0
                    diff[key] = [1] * (seq_len + 1)
                d = diff[key]
                p_start = (l - res) // k
                p_end = (r - res) // k
                d[p_start] = d[p_start] * v % MOD
                if p_end + 1 < len(d):
                    d[p_end + 1] = d[p_end + 1] * pow(v, MOD - 2, MOD) % MOD

        for (k, res), d in diff.items():
            mul = 1
            i = res
            p = 0
            while i < n:
                mul = mul * d[p] % MOD
                nums[i] = nums[i] * mul % MOD
                i += k
                p += 1

        return reduce(xor, nums)