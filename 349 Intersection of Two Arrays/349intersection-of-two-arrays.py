class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}

        for num in nums1:
            count[num] = 1 + count.get(num, 0)
        
        res = set()
        for num in nums2:
            if num in count:
                res.add(num)
        
        return [num for num in res]

# Time: O(n + m)
# Space: O(n + n)