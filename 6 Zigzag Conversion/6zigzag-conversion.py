class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ["" for _ in range(numRows)]
        curr_row = 0
        increase_row = False

        for c in s:
            res[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                increase_row = not increase_row
            if increase_row:
                curr_row += 1
            else:
                curr_row -= 1
        return "".join(res)

# Time: O(n)
# Space: O(n) due to res
        
