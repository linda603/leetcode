class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1: return [0]
        nums2 = [0] * n # array with original idx
        for i in range(n):
            nums2[i] = [nums[i], i]

        res = [0] * n

        def merge(left, right):
            nonlocal res
            i = j = 0
            merged = []
            count = 0 # inversion count

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    res[left[i][1]] += count
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += 1
                    j += 1
            while i < len(left):
                res[left[i][1]] += count
                merged.append(left[i])
                i += 1
            merged += right[j:]
            return merged
        
        def dfs(l, r):
            if l == r:
                return [nums2[l]]
            mid = (l + r) // 2
            left = dfs(l, mid)
            right = dfs(mid + 1, r)
            return merge(left, right)

        dfs(0, n - 1)
        return res

# Time: O(logn + logn*n) = O(nlogn)
# Space: O(logn + logn + n)