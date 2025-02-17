class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        curr_min = 1
        max_product = float("-inf")
        
        for num in nums:
            tmp = curr_max
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(tmp * num, curr_min * num, num) # curr_max is overwritten already
            max_product = max(max_product, curr_max)
        return max_product

# Time: O(n)
# Space: O(1)