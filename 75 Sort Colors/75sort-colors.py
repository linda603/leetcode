class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 # color 0
        r = len(nums) - 1 # color 2

        i = 0
        while i <= r:
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                continue
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            i += 1

# Time: O(n)
# Space: O(1)