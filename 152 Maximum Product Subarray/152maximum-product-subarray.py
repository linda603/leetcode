class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        curr = 1 # curr_product

        for i in range(len(nums)):
            curr *= nums[i]
            res = max(res, curr)
            if curr == 0:
                curr = 1
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            curr *= nums[i]
            res = max(res, curr)
            if curr == 0:
                curr = 1
        return res

# Time: O(2n)
# Space: O(1)