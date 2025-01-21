class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        res = 0

        total = 0
        for num in nums:
            total += num
            remain = total % k
            if remain in prefix_sum:
                res += prefix_sum[remain]
            prefix_sum[remain] = 1 + prefix_sum.get(remain, 0)
        return res

# Time: O(n)
# Space: O(n)