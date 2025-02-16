class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.house_rob(nums, 0, len(nums) - 2), self.house_rob(nums, 1, len(nums) - 1))
        
    def house_rob(self, nums, l, r):
        one = nums[r]
        two = 0

        for i in range(r - 1, l - 1, -1):
            tmp = one
            one = max(nums[i] + two, one)
            two = tmp
        return one

# Time: O(2n)
# Space: O(1)