class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[l] < nums[mid]: # left -> mid: sorted order, search in the right partition
                l = mid + 1
            else:
                r = mid - 1

# Time: O(logn)
# Space: O(1)