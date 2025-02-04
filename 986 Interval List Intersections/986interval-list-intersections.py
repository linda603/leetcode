class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort()
        secondList.sort()
        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            if start1 <= end2 and start2 <= end1:
                res.append([max(start1, start2), min(end1, end2)])
            if end1 <= end2:
                i += 1
            else:
                j += 1
        return res

# Time: O(nlogn + mlogm + n + m)
# Space: O(n + m)