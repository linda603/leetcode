class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_area = max(max_area, h * w)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area

# Time: O(n)
# Space: O(1)