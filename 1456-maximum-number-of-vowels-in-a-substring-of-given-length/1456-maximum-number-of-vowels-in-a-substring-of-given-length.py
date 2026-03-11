class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')

        count = sum(1 for c in s[:k] if c in vowels)
        max_count = count

        for i in range(k, len(s)):
            count += (1 if s[i] in vowels else 0)
            count -= (1 if s[i - k] in vowels else 0)

            max_count = max(max_count, count)
            if max_count == k:
                break
        return max_count

        