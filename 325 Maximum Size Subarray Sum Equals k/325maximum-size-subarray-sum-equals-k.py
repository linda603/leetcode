class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: -1}
        res = 0
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            diff = total - k
            if diff in prefix_sum:
                res = max(res, i - prefix_sum[diff])
            if total not in prefix_sum:
                prefix_sum[total] = i
        return res

# Time: O(n)
# Space: O(n)
