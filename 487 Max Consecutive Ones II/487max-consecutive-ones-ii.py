class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # sliding window
        # find the longest subarray with at most 1 zero
        res = 0
        cnt = 0

        l = 0
        for r in range(len(nums)):
            cnt += 1 - nums[r]
            while cnt > 1:
                cnt -= 1 - nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res

# Time: O(n)
# Space: O(1)