class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        l = len(nums) - 1 # first idx out of order
        r = 0 # last idx out of order

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                l = i
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                r = i + 1
        
        return r - l + 1 if l < r else 0

# Time: O(n)
# Space: O(1)