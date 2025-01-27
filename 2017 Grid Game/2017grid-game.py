class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_right = sum(grid[0])
        bottom_left = 0
        res = float("inf")

        for c in range(len(grid[0])):
            top_right -= grid[0][c]
            bottom_left += grid[1][c - 1] if c - 1 >= 0 else 0
            res = min(res, max(top_right, bottom_left))
        return res

# Time: O(n)
# Space: O(1)