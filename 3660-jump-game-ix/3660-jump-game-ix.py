class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # (l, r, mx)
        stack = []

        for i, x in enumerate(nums):
            l = i
            mx = x

            while stack and stack[-1][2] > x:
                pl, pr, pmx = stack.pop()

                l = pl
                mx = max(mx, pmx)

            stack.append((l, i, mx))

        ans = [0] * n

        for l, r, mx in stack:
            for i in range(l, r + 1):
                ans[i] = mx

        return ans