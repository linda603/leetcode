class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = {0: -1} # remainder: index
        res = 0

        total = 0
        for i, num in enumerate(nums):
            total += num
            remainder = total % k
            if remainder not in prefix_sum:
                prefix_sum[remainder] = i
            elif i - prefix_sum[remainder] >= 2:
                return True
        return False

# Time: O(n)
# Space: O(n)