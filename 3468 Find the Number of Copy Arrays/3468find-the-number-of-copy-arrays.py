class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        left, right = bounds[0] # range of first number

        for i in range(1, len(bounds)):
            diff = original[i] - original[i - 1]
            # Update new bound for the next number at i
            left += diff
            right += diff
            left = max(left, bounds[i][0])
            right = min(right, bounds[i][1])
        return right - left + 1 if left <= right else 0

# Time: O(n)
# Space: O(1)