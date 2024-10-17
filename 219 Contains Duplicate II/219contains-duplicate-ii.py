class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}

        l = 0
        for r in range(len(nums)):
            if r - l > k:
                del window[nums[l]]
                l += 1
            if nums[r] in window:
                return True
            window[nums[r]] = True
        return False

# Time: O(n)
# Space: O(n)