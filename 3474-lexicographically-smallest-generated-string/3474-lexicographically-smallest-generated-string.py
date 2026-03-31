class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total = n + m - 1
        word = ['a'] * total
        locked = [False] * total

        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    ch = str2[j]
                    if locked[pos] and word[pos] != ch:
                        return ""
                    word[pos] = ch
                    locked[pos] = True

        for i in range(n):
            if str1[i] == 'F':
                match = all(word[i + j] == str2[j] for j in range(m))

                if match:
                    changed = False
                    for j in range(m - 1, -1, -1):  
                        pos = i + j
                        if not locked[pos]:
                            word[pos] = 'a' if str2[j] != 'a' else 'b'
                            changed = True
                            break
                    if not changed:
                        return ""

        return "".join(word)