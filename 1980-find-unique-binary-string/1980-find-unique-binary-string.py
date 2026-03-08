class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        for i, s in enumerate(nums):
            result.append('0' if  s[i] == '1' else '1')
        return ''.join(result)
        