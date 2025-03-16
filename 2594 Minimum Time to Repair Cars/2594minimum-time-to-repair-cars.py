class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = min(ranks)
        r = min(ranks) * cars * cars
        res = r

        while l <= r:
            mid = (l + r) // 2
            if self.is_valid(ranks, cars, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def is_valid(self, ranks, cars, time):
        count = 0

        for rank in ranks:
            count += int(sqrt(time // rank))

        return count >= cars