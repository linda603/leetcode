class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map = {}
        for i, num in enumerate(nums1):
            idx_map[num] = i

        # monotonic decreasing stack
        stack = []
        res = [-1] * len(nums1)
        for num in nums2:
            while stack and stack[-1] < num:
                i = idx_map[stack.pop()]
                res[i] = num
            if num in idx_map:
                stack.append(num)
        return res

# Time: O(n1 + n2)
# Space: O(n1 + n2)