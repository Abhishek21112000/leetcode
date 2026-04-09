class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # unlocked = {0}
        # changed = True 
        # while changed:
        #     changed = False
        #     for room in unlocked.copy():
        #         for key in rooms[room]:
        #             if key not in unlocked:
        #                 unlocked.add(key)
        #                 changed = True
        # return len(unlocked) == len(rooms)

        #DFS

        visit = set()
        stack = [0]

        while stack:
            room = stack.pop()
            if room in visit:
                continue
            visit.add(room)
            for key in rooms[room]:
                if key not in visit:
                    stack.append(key)
        return len(visit) == len(rooms)

        
        