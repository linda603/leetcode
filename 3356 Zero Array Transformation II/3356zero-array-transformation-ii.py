class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        events = [0] * (len(nums) + 1)
        count = 0
        j = 0

        for i, num in enumerate(nums):
            while j < len(queries) and count + events[i] < num:
                print("i, events[i], count:", i, events[i], count)
                l, r, val = queries[j]
                events[max(l, i)] += val
                events[r + 1] -= val
                j += 1
            if count + events[i] < num:
                return -1
            count += events[i]

        return j

# Time: O(n + j)
# Space: O(n)