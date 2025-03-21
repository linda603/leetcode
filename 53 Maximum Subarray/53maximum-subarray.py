class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        total = 0

        for num in nums:
            if total < 0:
                total = 0
            total += num
            res = max(res, total)
        return res

# Time: O(n)
# Space: O(1)