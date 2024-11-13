class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        res = 0
        nums.sort()

        for i, num in enumerate(nums):
            # find the largest number x - idx left, where x + nums[i] < upper + 1, in case x has duplicated vals
            # find the largest number y - idx right, where x + nums[i] < lower
            left = self.binary_search(nums, i + 1, n - 1, lower - num) + 1
            right = self.binary_search(nums, i + 1, n - 1, upper + 1 - num)
            res += right - left + 1
        return res

    def binary_search(self, nums, l, r, target):
        res = l - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

# Time: O(nlogn + n2logn)
# Space: O(n)