class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        res = 0

        right = nums[n - 1]
        for i in range(n - 1, -1, -1):
            right = max(right, nums[i])
            right_max[i] = right
        
        l = 0
        for r in range(1, n):
            while l < r and nums[l] > right_max[r]:
                l += 1
            if nums[l] <= nums[r]:
                res = max(res, r - l)
        return res

# Time: O(n)
# Space: O(n)