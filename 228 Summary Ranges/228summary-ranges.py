class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(nums[i]))
            i += 1
        return res

#Time: O(n)
#Space: O(n) due to res