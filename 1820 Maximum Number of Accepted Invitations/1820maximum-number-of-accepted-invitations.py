class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        matches = {} #girl: boy. To store matches formed

        # A dfs to match a boy at index boy with potential girls.
        def dfs(boy, visited):
            
            for girl in range(COLS):
                """
                Rule 1: If girl is not taken, girl will accept the invitation
                Rule 2: If girl is taken, boy can ask her partner to find a new girl
                """
                if grid[boy][girl] == 1 and girl not in visited:
                    visited.add(girl)
                    if girl not in matches or dfs(matches[girl], visited):
                        matches[girl] = boy
                        return True

            return False

        
        for boy in range(ROWS):
            dfs(boy, set())
        return len(matches)

#Time: O(m*n*n)
#Space: O(n)