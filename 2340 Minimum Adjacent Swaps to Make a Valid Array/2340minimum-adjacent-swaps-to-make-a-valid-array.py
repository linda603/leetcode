class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        #valid array, no need to swap
        if not nums or len(nums) == 1:
            return 0

        maxVal, minVal = float("-inf"), float("inf")
        maxIdx, minIdx = 0, 0
        for i, num in enumerate(nums):
            if num >= maxVal:
                maxIdx = i
                maxVal = num
            if num < minVal:
                minIdx = i
                minVal = num
        
        return len(nums) - 1 - maxIdx + minIdx if minIdx < maxIdx else len(nums) - 2 - maxIdx + minIdx

#Time: O(n)
#Space: O(1)