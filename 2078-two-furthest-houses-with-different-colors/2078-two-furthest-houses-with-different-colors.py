class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        
        for i in range(n):
            for j in range(n - 1, i, -1):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
                    break   
        
        return ans