class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):
            rightSum = totalSum - leftSum - num
            if leftSum == rightSum:
                return i
            leftSum += num
        return -1