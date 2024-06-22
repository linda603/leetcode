class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                self.flip(nums, i)
                res += 1
    
        for i in range(len(nums) - 2, len(nums)):
            if nums[i] == 0:
                return -1
        
        return res
    
    def flip(self, nums, i):
        for i in range(i, i + 3):
            nums[i] = not nums[i]