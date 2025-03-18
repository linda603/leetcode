class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            if self.can_finish(piles, h, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def can_finish(self, piles, h, speed):
        hours = 0

        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h

# Time: O(log(max(piles)))
# Space: O(1)