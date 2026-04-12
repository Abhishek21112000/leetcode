class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1:
                return 0
            
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        dp = {-1: 0}

        for i in range(len(word) - 1):
            cur = ord(word[i]) - ord('A')
            nxt = ord(word[i + 1]) - ord('A')
            new_dp = {}

            for other, cost in dp.items():
                move1 = cost + dist(cur, nxt)
                key1 = other
                new_dp[key1] = min(new_dp.get(key1, float('inf')), move1)

                move2 = cost + dist(other, nxt)
                key2 = cur
                new_dp[key2] = min(new_dp.get(key2, float('inf')), move2)

            dp = new_dp

        return min(dp.values())