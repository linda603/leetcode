class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort

        def merge_lists(left, right):
            res = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res += left[i:]
            res += right[j:]
            return res

        def merge_sort(l, r):
            if l == r:
                return [nums[l]]
            mid = (l + r) // 2
            left = merge_sort(l, mid)
            right = merge_sort(mid + 1, r)
            return merge_lists(left, right)

        return merge_sort(0, len(nums) - 1)

# Time: O(logn + nlogn) = O(nlogn)
# Space: O(n) due to merge_lists
