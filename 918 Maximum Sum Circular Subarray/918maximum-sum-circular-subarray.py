class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]

        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        if max_sum < 0:
            return max_sum
        return max(max_sum, sum(nums) - min_sum)

# Time: O(n)
# Space: O(1)