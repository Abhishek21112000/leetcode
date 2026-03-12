from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        must_edges = [(u, v, s) for u, v, s, m in edges if m == 1]
        opt_edges  = [(u, v, s) for u, v, s, m in edges if m == 0]

        must_components = n
        for u, v, s in must_edges:
            if not union(u, v):
                return -1
            must_components -= 1

        saved_parent = parent[:]
        saved_rank   = rank[:]

        candidates = sorted({val for u, v, s in must_edges for val in (s,)}
                          | {val for u, v, s in opt_edges for val in (s, 2 * s)})

        def feasible(lim: int) -> bool:
            if any(s < lim for u, v, s in must_edges):
                return False

            p, r = saved_parent[:], saved_rank[:]

            def find2(x):
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x

            def union2(x, y):
                px, py = find2(x), find2(y)
                if px == py:
                    return False
                if r[px] < r[py]:
                    px, py = py, px
                p[py] = px
                if r[px] == r[py]:
                    r[px] += 1
                return True

            free, upgrade = [], []
            for u, v, s in opt_edges:
                if s >= lim:
                    free.append((u, v))
                elif 2 * s >= lim:
                    upgrade.append((u, v))

            comp = must_components
            for u, v in free:
                if union2(u, v):
                    comp -= 1

            upgrades_used = 0
            for u, v in upgrade:
                if comp == 1:
                    break
                if union2(u, v):
                    comp -= 1
                    upgrades_used += 1

            return comp == 1 and upgrades_used <= k

        if not feasible(1):
            return -1

        lo, hi, ans = 0, len(candidates) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(candidates[mid]):
                ans = candidates[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans