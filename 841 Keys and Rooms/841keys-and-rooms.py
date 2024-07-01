class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [] # List of keys to open the room
        stack.append(0)
        visited = set()
        visited.add(0)

        while stack:
            curr = stack.pop()
            for key in rooms[curr]:
                if key in visited:
                    continue
                visited.add(key)
                stack.append(key)
        
        return len(visited) == len(rooms)

#Time: O(n*keys), n: number of rooms, keys: number of total of keys
#Space: O(n)