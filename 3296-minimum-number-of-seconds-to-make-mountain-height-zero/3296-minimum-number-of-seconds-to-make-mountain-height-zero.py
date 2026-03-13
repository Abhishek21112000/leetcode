import math
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def max_reduction(w, T):
            discriminant = 1 + 8 * T / w
            return int((-1 + math.sqrt(discriminant))/2)
        
        def can_finish(T):
            total = sum(max_reduction(w, T) for w in workerTimes)
            return total >= mountainHeight
        
        lo = 1
        hi = max(workerTimes) * mountainHeight * (mountainHeight + 1 ) // 2

        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1 

        return lo 

        