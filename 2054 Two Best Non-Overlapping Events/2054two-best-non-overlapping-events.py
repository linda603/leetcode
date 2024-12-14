class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        line_sweep = []
        res = 0
        max_val = 0 # represents max_val of ending point

        for start, end, val in events:
            line_sweep.append([start, True, val])
            line_sweep.append([end + 1, False, val])
        line_sweep.sort()

        for time, is_start, val in line_sweep:
            if is_start:
                res = max(res, val + max_val)
            else:
                max_val = max(max_val, val)
        return res

# Time: O(n + nlogn) = O(nlogn)
# Space: O(n)