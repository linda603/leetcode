class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh_oranges:
            time += 1
            len_q = len(queue)
            for i in range(len_q):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if nei_r in range(rows) and nei_c in range(cols) and grid[nei_r][nei_c] == 1:
                        queue.append((nei_r, nei_c))
                        grid[nei_r][nei_c] = 2
                        fresh_oranges -= 1
        return time if fresh_oranges == 0 else -1

#Time: O(mn)
#Space: O(mn)