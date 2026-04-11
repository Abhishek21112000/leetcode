class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)
        
        ans = float('inf')

        for idx_list in indices.values():
            if len(idx_list) < 3:
                continue

            for i in range(len(idx_list) - 2):
                dist = 2 * (idx_list[i+2] - idx_list[i])
                ans = min(ans, dist)
        return ans if ans != float('inf') else -1
        