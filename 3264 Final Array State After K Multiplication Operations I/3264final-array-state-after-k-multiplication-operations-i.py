class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            min_idx = self.get_min_idx(nums)
            nums[min_idx] *= multiplier
            k -= 1
        return nums
    
    def get_min_idx(self, nums):
        min_val = float("inf")
        min_idx = 0

        for i in range(len(nums)):
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i
        return min_idx

# Time: O(k*n)
# Space: O(1)