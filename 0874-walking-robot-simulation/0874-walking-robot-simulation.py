class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        directions = [(0,1), (1,0), (0, -1), (-1,0 )]
        x, y = 0, 0
        dir_idx = 0
        max_dist = 0

        for cmd in commands:
            if cmd == -2:
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:
                dir_idx = (dir_idx + 1) % 4
            else:
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    next_x , next_y = x + dx , y + dy
                    if(next_x , next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_dist = max(max_dist, x*x + y*y)
                    else:
                        break
        return max_dist


