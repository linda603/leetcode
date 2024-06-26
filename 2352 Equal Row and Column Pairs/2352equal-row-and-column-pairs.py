class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {} #row: 1

        for r in grid:
            row = tuple(r)
            if row not in count:
                count[row] = 0
            count[row] += 1
        
        res = 0
        for c in range(len(grid)):
            col = tuple([grid[i][c] for i in range(len(grid))])
            if col in count:
                res += count[col]
        
        return res

#Time: O(n^2)
#Space: O(n^2)