class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 2
            else:
                i += 1

        i = j = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
        return nums

# Time: O(2n)
# Space: O(1)