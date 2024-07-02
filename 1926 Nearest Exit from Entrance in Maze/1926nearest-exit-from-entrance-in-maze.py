class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        res = 0
        ROWS, COLS = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1]))
        #visited = set()
        #visited.add((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = "+"
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            qLen = len(queue)
            for i in range(qLen):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(ROWS) and c in range(COLS) and \
                        maze[r][c] == ".":
                        # If at valid exit either at start row, end row, start col, end col. Return the curr level
                        if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                            res += 1
                            return res
                        queue.append((r, c))
                        maze[r][c] = "+"
            res += 1 # Increment res after we finish 1 level
        return -1

#Time: O(m*n)
#Space: O(m*n) -> O(min(m, n)) if don't use visited set