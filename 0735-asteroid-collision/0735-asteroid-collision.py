class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for  ast in asteroids:
            alive = True
            while alive and ast < 0 and stack and stack[-1] > 0:
                top = stack[-1]
                if top < abs(ast):
                    stack.pop()
                elif top == abs(ast):
                    stack.pop()
                    alive = False
                else: 
                    alive = False
            if alive:
                stack.append(ast)
        return stack