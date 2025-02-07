class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0

        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                res = max(res, curr)
                curr = nums[i]
        return max(res, curr)

# Time: O(n)
# Space: O(1)