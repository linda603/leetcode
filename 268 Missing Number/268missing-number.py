class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #[3, 0, 1]
        # sum of [0, 1, 2, 3] - sum of [3, 0, 1] = missing number
        total = 0

        for num in range(len(nums) + 1):
            total += num
        
        for num in nums:
            total -= num

        return total

#Time: O(2n)
#Space: O(1)