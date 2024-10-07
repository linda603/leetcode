class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        
        for num in nums:
            i = abs(num) - 1
            if i >= 0 and i < len(nums):
                if nums[i] > 0:
                    nums[i] *= -1
                elif nums[i] == 0:
                    nums[i] = -1 * (len(nums) + 1) # change to negative that does not affect to the solution
                else: # nums[i] < 0 -> i + 1 already exist
                    continue
    
        for num in range(1, len(nums) + 1):
            i = num - 1
            if nums[i] >= 0:
                return num
        return len(nums) + 1

#Time: O(3n)
#Space: O(1)