class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums) - 1):
            res = max(res, abs(nums[i + 1] - nums[i]))
        res = max(res, abs(nums[len(nums) - 1] - nums[0]))
        return res

# Time: O(n)
# Space: O(1)