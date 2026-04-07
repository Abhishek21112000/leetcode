from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = []        
        self.i = 0
        self.is_origin = True

        self.pos.append((0, 0, "South"))          

        for x in range(1, width):
            self.pos.append((x, 0, "East"))

        for y in range(1, height):
            self.pos.append((width - 1, y, "North"))

        for x in range(width - 2, -1, -1):
            self.pos.append((x, height - 1, "West"))

        for y in range(height - 2, 0, -1):
            self.pos.append((0, y, "South"))

        self.m = len(self.pos)          
    def step(self, num: int) -> None:
        self.is_origin = False
        self.i = (self.i + num) % self.m

    def getPos(self) -> List[int]:
        return [self.pos[self.i][0], self.pos[self.i][1]]

    def getDir(self) -> str:
        if self.is_origin:
            return "East"
        return self.pos[self.i][2]