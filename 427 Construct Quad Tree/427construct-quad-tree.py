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
        
        def dfs(r, c, n):
            all_match = self.check_all_match(grid, r, c, n)
            if all_match:
                return Node(grid[r][c], True, None, None, None, None)
            n = n // 2
            top_left = dfs(r, c, n)
            top_right = dfs(r, c + n, n)
            bottom_left = dfs(r + n, c, n)
            bottom_right = dfs(r + n, c + n, n)
            return Node(grid[r][c], False, top_left, top_right, bottom_left, bottom_right)
        
        return dfs(0, 0, len(grid))
    
    def check_all_match(self, grid, r, c, n):
        for i in range(n):
            for j in range(n):
                if grid[r][c] != grid[r + i][c + j]:
                    return False
        return True

# Time: O(logn*4*n^2) = O(nlogn). Length of every dfs reduces to half. 
#       Every recursion, need to check all values in the grid if they have the same values.
# Space: O(logn). Depth of dfs()