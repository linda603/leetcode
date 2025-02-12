"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def same_val(r, c, n):
            val = grid[r][c]

            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != val:
                        return False
            return True
        
        def dfs(r, c, n):
            if same_val(r, c, n):
                return Node(grid[r][c], 1, None, None, None, None)
            n = n // 2
            top_left = dfs(r, c, n)
            top_right = dfs(r, c + n, n)
            bottom_left = dfs(r + n, c, n)
            bottom_right = dfs(r + n, c + n, n)
            return Node(grid[r][c], 0, top_left, top_right, bottom_left, bottom_right)

        return dfs(0, 0, len(grid))

# Time: O(n^2logn)
# Space: O(logn)