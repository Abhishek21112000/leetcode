
from collections import defaultdict, deque
from math import isqrt

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)

        
        spf = list(range(max_val + 1))
        for i in range(2, isqrt(max_val) + 1):
            if spf[i] == i:
                step = i
                start = i * i
                for j in range(start, max_val + 1, step):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x: int) -> bool:
            return x >= 2 and spf[x] == x

        
        divisible = defaultdict(list)

        for idx, x in enumerate(nums):
            temp = x
            factors = set()
            while temp > 1:
                p = spf[temp]
                factors.add(p)
                while temp % p == 0:
                    temp //= p
            for p in factors:
                divisible[p].append(idx)

      
        q = deque()
        q.append((0, 0))          
        visited = [False] * n
        visited[0] = True

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

       
            for nxt in (i - 1, i + 1):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps + 1))

            
            val = nums[i]
            if is_prime(val):
                indices = divisible[val]       
                if indices:
                    for nxt in indices:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append((nxt, steps + 1))
                    divisible[val] = []       
        return -1