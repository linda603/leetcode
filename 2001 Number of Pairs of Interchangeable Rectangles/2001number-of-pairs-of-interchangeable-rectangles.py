class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        freqs = {} #ratio: count
        result = 0

        for rectangle in rectangles:
            ratio = rectangle[0] / rectangle[1]
            if ratio not in freqs:
                freqs[ratio] = 0
            freqs[ratio] += 1
        
        for count in freqs.values():
            if count > 1:
                result += (count * (count - 1)) // 2
        return result

#Time: O(n)
#Space: O(n)
