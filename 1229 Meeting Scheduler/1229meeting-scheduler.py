class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        i = j = 0

        while i < len(slots1) and j < len(slots2):
            start1, end1 = slots1[i]
            start2, end2 = slots2[j]
            if start1 < end2 and start2 < end1: # intersection happens
                if min(end1, end2) - max(start1, start2) >= duration:
                    return [max(start1, start2), max(start1, start2) + duration]
            if end1 <= end2:
                i += 1
            else:
                j += 1
        return []

# Time: O(nlogn + mlogm)
# Space: O(n + m)