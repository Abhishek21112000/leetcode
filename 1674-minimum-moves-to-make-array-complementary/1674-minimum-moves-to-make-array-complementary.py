class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        n = len(nums)

        # difference array
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a, b)
            y = max(a, b)

            # initially assume 2 moves
            diff[2] += 2

            # 2 -> 1
            diff[x + 1] -= 1

            # 1 -> 0
            diff[x + y] -= 1

            # 0 -> 1
            diff[x + y + 1] += 1

            # 1 -> 2
            diff[y + limit + 1] += 1

        ans = float('inf')
        cur = 0

        for s in range(2, 2 * limit + 1):
            cur += diff[s]
            ans = min(ans, cur)

        return ans