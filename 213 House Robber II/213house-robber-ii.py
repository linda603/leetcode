class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(self.rob_house(nums, 0, len(nums) - 1), self.rob_house(nums, 1, len(nums)))
        
    def rob_house(self, nums, l, r):
        n = r
        one = nums[n - 1]
        two = 0

        for i in range(n - 2, l - 1, -1):
            tmp = one
            one = max(nums[i] + two, one)
            two = tmp
        return one

# Time: O(2n)
# Space: O(1)