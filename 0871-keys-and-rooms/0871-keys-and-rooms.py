class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(node):
            for room in rooms[node]:
                if room not in seen:
                    seen.add(room)
                    dfs(room)

        
        seen = {0}
        dfs(0)
        if len(seen) == len(rooms):
            return True
        else:
            return False