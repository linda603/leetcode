class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1

        # find the largest index i that nums[i] < nums[i + 1]. This is the break point
        for i in range(len(nums) - 2, -1, -1): 
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # if no i exists, reverse nums
        if pivot == -1:
            nums.reverse() # nums = [5, 4, 3, 2, 1] -> return [1, 2, 3, 4, 5]
        else:
            # find greater element than pivot index in the right partition and swap val to pivot val
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[pivot]:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    break
            
            # Sort the right partition to increasing order
            self.reverse_sort(nums, pivot + 1, len(nums) - 1)
        return
    
    def reverse_sort(self, nums, start, end):
        l = start
        r = end
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

#Time: O(n + n + n) = O(3n) = O(n)
#Space: O(1)