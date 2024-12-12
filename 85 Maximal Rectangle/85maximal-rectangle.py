class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0

        for row in matrix:
            for c in range(len(row)):
                if row[c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            curr_max_rectangle = self.max_rectangle(heights)
            res = max(res, curr_max_rectangle)
        return res
        
    def max_rectangle(self, heights):
        res = 0
        stack = [-1]

        for i, h in enumerate(heights):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                curr_area = height * width
                res = max(res, curr_area)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            curr_area = height * width
            res = max(res, curr_area)
        return res

# Time: O(mn)
# Space: O(n)