class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]
        
    def binary_search(self, nums, target, is_left):
        l = 0
        r = len(nums) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                res = mid
                if is_left:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res

# Time: O(2log(n)). n: len(nums)
# Space: O(1)