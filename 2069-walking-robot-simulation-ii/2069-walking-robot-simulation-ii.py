from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = []          # stores (x, y, direction) for each perimeter step
        self.i = 0
        self.is_origin = True

        # Build the path along the perimeter, starting from (0,0) facing South
        # (the direction it will be facing after arriving there)
        self.pos.append((0, 0, "South"))          # start corner

        # Bottom edge (East direction)
        for x in range(1, width):
            self.pos.append((x, 0, "East"))

        # Right edge (North direction)
        for y in range(1, height):
            self.pos.append((width - 1, y, "North"))

        # Top edge (West direction)
        for x in range(width - 2, -1, -1):
            self.pos.append((x, height - 1, "West"))

        # Left edge (South direction)
        for y in range(height - 2, 0, -1):
            self.pos.append((0, y, "South"))

        self.m = len(self.pos)          # total perimeter steps
        # Note: self.m = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        self.is_origin = False
        # Move forward num steps along the precomputed cycle
        self.i = (self.i + num) % self.m

    def getPos(self) -> List[int]:
        # Return the current (x, y) position
        return [self.pos[self.i][0], self.pos[self.i][1]]

    def getDir(self) -> str:
        # Special case: if the robot has never moved, it still faces East
        if self.is_origin:
            return "East"
        return self.pos[self.i][2]