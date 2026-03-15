MOD = 10**9 + 7
class Fancy:

    def __init__(self):
        self.seq = []
        self.mult = 1
        self.add = 0

    def append(self, val: int) -> None:
        norm = (val - self.add) * pow(self.mult, MOD - 2, MOD) % MOD
        self.seq.append(norm)
        

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD
        

    def multAll(self, m: int) -> None:
        self.mult = self.mult * m % MOD
        self.add = self.add * m  % MOD        

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % MOD        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)