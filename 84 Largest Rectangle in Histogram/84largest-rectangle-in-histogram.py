class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [-1]

        for i, height in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > height: # cannot extend further with curr_height
                prev_height = heights[stack.pop()]
                area = prev_height * (i - stack[-1] - 1)
                res = max(res, area)
            stack.append(i)
        while stack[-1] != -1:
            prev_height = heights[stack.pop()]
            area = prev_height * (len(heights) - stack[-1] - 1)
            res = max(res, area)
        return res

# Time: O(n)
# Space: O(n)