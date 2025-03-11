class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        intervals = [(0, 0)]
        for start, end in zip(startTime, endTime):
            intervals.append((start, end))
        intervals.append((eventTime, eventTime))
        free = []

        for i in range(len(intervals) - 1):
            start1, end1 = intervals[i]
            start2, end2 = intervals[i + 1]
            if end1 < start2:
                free.append(start2 - end1)
            else:
                free.append(0)
        # free = [1, 1, 1] k = 1 -> window = 2
        # free = [0, 1, 5, 1] k = 1

        res = 0
        curr = 0
        for i in range(min(len(free), k + 1)):
            curr += free[i]
        res = max(res, curr)
        for i in range(k + 1, len(free)):
            curr -= free[i - k - 1]
            curr += free[i]
            res = max(res, curr)
        return res

# Time: O(n)
# Space: O(n)