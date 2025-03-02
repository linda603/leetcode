class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            if id1 < id2:
                res.append([id1, val1])
                i += 1
            elif id1 > id2:
                res.append([id2, val2])
                j += 1
            else:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
        res += nums1[i:]
        res += nums2[j:]
        return res

# Time: O(m + n)
# Space: O(m + n)