class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 1

        l = 0
        for r in range(len(nums)):
            curr *= nums[r]
            while l <= r and curr >= k:
                curr //= nums[l]
                l += 1
            res += r - l + 1 if l <= r else 0
        return res

# Time: O(n)
# Space: O(1)