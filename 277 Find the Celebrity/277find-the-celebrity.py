# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        top = 0
        bottom = n - 1

        while top < bottom:
            if knows(top, bottom):
                top += 1
            elif knows(bottom, top):
                bottom -= 1
            else:
                # None of them cannot be a celeb
                top += 1
                bottom -= 1
        if top > bottom:
            return -1
            
        celeb = top
        for i in range(n):
            if i == celeb:
                continue
            if knows(celeb, i) or not knows(i, celeb):
                return -1
        return celeb

# Time: O(n + n) = O(n)
# Space: O(1)