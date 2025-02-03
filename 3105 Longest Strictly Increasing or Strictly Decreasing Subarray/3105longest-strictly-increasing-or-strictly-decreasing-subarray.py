class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        inc = dec = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            max_len = max(max_len, inc, dec)
        return max_len

# Time: O(n)
# Space: O(1)