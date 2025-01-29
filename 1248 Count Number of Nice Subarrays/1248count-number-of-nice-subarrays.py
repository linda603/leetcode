class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1} # prefix sum of odd numbers
        curr_odd = 0
        res = 0
        
        for num in nums:
            if num % 2:
                curr_odd += 1
            diff = curr_odd - k
            if diff in prefix_sum:
                res += prefix_sum[diff]
            prefix_sum[curr_odd] = 1 + prefix_sum.get(curr_odd, 0)
        return res

# Time: O(n)
# Space: O(n)