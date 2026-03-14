class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.result = ""
        
        def backtrack(current):
            if self.result:  # early exit
                return
            if len(current) == n:
                self.count += 1
                if self.count == k:
                    self.result = current
                return
            
            for char in 'abc':
                if not current or current[-1] != char:
                    backtrack(current + char)
        
        backtrack("")
        return self.result