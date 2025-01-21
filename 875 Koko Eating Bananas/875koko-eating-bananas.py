class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if self.is_valid(piles, h, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

    def is_valid(self, piles, h, speed):
        cnt = 0

        for p in piles:
            cnt += math.ceil(p / speed)
        return cnt <= h

# Time: O(log(sum(piles)))
# Space: O(1)