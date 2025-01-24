class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad_idx = -1 # most recent idx with value out of bound [minK, maxK]
        left = -1 # the most recent index with value = minK
        right = -1 #                                 = maxK
        res = 0

        for i, num in enumerate(nums):
            if nums[i] < minK or nums[i] > maxK:
                bad_idx = i
            if nums[i] == minK:
                left = i
            if nums[i] == maxK:
                right = i
            res += max(0, min(left, right) - bad_idx)
        return res

# Time: O(n)
# Space: O(1)