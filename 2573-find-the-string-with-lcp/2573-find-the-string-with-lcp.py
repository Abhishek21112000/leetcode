class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        pattern = [''] * n

        char = 0
        for i in range(n):
            if pattern[i]:
                continue
            if char >= 26:
                return ""
            pattern[i] = chr(ord('a') + char)
            char += 1 
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    pattern[j] = pattern[i]
        check = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if pattern[i] == pattern[j]:
                    if i == n -1 or j == n -1 :
                        check[i][j] = 1
                    else:
                        check[i][j] = check[i + 1][j + 1] + 1
                if check[i][j] != lcp[i][j]:
                    return ""
        return ''.join(pattern)

        