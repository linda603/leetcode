class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        
        level = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nei_r = r + dr
                    nei_c = c + dc
                    if nei_r in range(m) and nei_c in range(n) and rooms[nei_r][nei_c] == 2147483647:
                        rooms[nei_r][nei_c] = level
                        queue.append((nei_r, nei_c))
            level += 1

# Time: O(mn + mn)
# Space: O(mn) due to queue size