class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                curr_area = min_height * (j - i + 1)
                res = max(res, curr_area)
        return res

# Time: O(n^2)
# Space: O(1)