# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # definition of celebrity: every knows this node. this node does not know any one
        top = 0
        bottom = n - 1

        while top < bottom:
            if knows(top, bottom): # top is not a celebrity, eleminate this node
                top += 1
            elif knows(bottom, top):
                bottom -= 1
            else:
                # either of them can be a celeb
                top += 1
                bottom -= 1
        if top > bottom:
            return -1

        # top = bottom. Need to check the row to make sure: does not know any one
        #                                 col             : every one know this celeb
        pos_celeb = top
        for c in range(n):
            if c == pos_celeb:
                continue
            if knows(pos_celeb, c):
                return -1
        for r in range(n):
            if r == pos_celeb:
                continue
            if not knows(r, pos_celeb):
                return -1
        return pos_celeb

# Time: O(n + n + n) = O(n)
# Space: O(1)