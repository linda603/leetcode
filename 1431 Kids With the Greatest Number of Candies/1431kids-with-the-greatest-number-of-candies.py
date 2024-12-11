class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        res = [False] * len(candies)

        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_candy:
                res[i] = True
        return res

# Time: O(n)
# Space: O(n)