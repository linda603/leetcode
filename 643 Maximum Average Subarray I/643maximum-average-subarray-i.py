class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")
        total = 0

        l = 0
        for r in range(len(nums)):
            total += nums[r]
            if r - l + 1 == k:
                res = max(res, total / k)
                total -= nums[l]
                l += 1
        return res

# Time: O(n)
# Space: O(1)