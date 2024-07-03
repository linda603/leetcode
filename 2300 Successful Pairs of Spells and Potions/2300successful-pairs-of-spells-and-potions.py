class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for s in spells:
            mostLeft = len(potions)
            l = 0
            r = len(potions) - 1

            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * s >= success:
                    mostLeft = mid
                    r = mid - 1
                else:
                    l = mid + 1
            res.append(len(potions) - mostLeft)
        return res

#Time: O(nlogn + mlogn) = O((m+n)*logn) m: len(spells), n: len(potions)
#Space: O(n)