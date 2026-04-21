from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(list)

        for i in range(n):
            groups[find(i)].append(i)

        ans = 0

        for indices in groups.values():
            freq = Counter(source[i] for i in indices)

            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1

        return ans