class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        res = 0

        total = 0
        for num in nums:
            total += num
            diff = total - k
            if diff in prefix_sum:
                res += prefix_sum[diff]
            prefix_sum[total] = 1 + prefix_sum.get(total, 0)
        return res

# Time: O(n)
# Space: O(n)