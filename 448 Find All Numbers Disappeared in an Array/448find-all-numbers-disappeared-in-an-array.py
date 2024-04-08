class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        n = len(nums)
        hashMap = {i: True for i in range(1, n + 1)}

        for num in nums:
            if num in hashMap:
                hashMap.pop(num)
        return list(hashMap.keys())

#Time: O(n)
#Space: O(n)
"""
        result = []
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])
        
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)
        return result

#Time: O(n)
#Space: O(1)