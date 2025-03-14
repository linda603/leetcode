class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        line_sweep = [0] * (len(nums) + 1)
        count = 0
        k = 0

        for i, num in enumerate(nums):
            while k < len(queries) and count + line_sweep[i] < num:
                start, end, val = queries[k]
                k += 1
                if end < i:
                    continue
                line_sweep[max(i, start)] += val
                line_sweep[end + 1] -= val
            if count + line_sweep[i] < num:
                return -1
            count += line_sweep[i]
        return k

# Time: O(n + k)
# Space: O(n)