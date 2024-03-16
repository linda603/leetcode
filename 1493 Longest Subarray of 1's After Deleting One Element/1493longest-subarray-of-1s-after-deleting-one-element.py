class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        currLength = 0
        maxLength = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            currLength = right - left
            maxLength = max(currLength, maxLength)
        return maxLength
