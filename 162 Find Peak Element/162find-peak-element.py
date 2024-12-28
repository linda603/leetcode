class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid + 1)
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]):
                return mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1

# Time: O(logn)
# Space: O(1)
