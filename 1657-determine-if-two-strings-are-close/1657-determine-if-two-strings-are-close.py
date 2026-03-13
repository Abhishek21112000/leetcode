from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1, freq2 = Counter(word1), Counter(word2)
        return freq1.keys() == freq2.keys() and \
               sorted(freq1.values()) == sorted(freq2.values())