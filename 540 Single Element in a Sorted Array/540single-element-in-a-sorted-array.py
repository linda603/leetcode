class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if ((mid - 1 < 0 or nums[mid - 1] != nums[mid]) and 
                (mid + 1 == len(nums) or nums[mid] != nums[mid + 1])):
                return nums[mid]
            leftLen = mid - l if nums[mid] == nums[mid + 1] else mid - l - 1
            if leftLen % 2:
                r = mid - 1 if nums[mid] == nums[mid + 1] else mid - 2
            else:
                l = mid + 2 if nums[mid] == nums[mid + 1] else mid + 1

#Time: O(logn)
#Space: O(1) 