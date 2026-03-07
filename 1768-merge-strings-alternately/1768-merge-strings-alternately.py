from itertools import zip_longest

class Solution(object):
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))

    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     result = []
    #     i, j = 0, 0

    #     while i < len(word1) and j < len(word2):
    #         result.append(word1[i])
    #         result.append(word2[j])
    #         i += 1
    #         j += 1

    #     result.append(word1[i:])
    #     result.append(word2[j:])

    #     return "".join(result)