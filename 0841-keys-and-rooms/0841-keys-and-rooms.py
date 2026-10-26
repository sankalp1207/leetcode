class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = {0}
        stk = [0]
        while stk:
            curr = stk .pop()
            for key in rooms[curr]:
                if key not in visited:
                    visited.add(key)
                    stk.append(key)
        if len(rooms) == len(visited):
            return True
        else:
            return False