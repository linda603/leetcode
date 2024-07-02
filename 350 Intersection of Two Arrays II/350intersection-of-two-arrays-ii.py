class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = collections.Counter(nums1)
        res = []

        for num in nums2:
            if num in freq1:
                res.append(num)
                freq1[num] -= 1

                if freq1[num] == 0:
                    del freq1[num]
        return res

#Time: O(m + n)
#Space: O(max(m,n))