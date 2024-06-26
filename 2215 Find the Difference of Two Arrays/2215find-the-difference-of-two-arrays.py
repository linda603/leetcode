class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [set(), set()]

        for num in nums1:
            if num not in nums2:
                res[0].add(num)
        
        for num in nums2:
            if num not in nums1:
                res[1].add(num)
        
        return res

#Time: O(m + n)
#Space: O(m + n)