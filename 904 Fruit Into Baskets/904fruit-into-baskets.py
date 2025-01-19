class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        types = {}

        l = 0
        for r in range(len(fruits)):
            types[fruits[r]] = 1 + types.get(fruits[r], 0)
            while len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res

# Time: O(n)
# Space: O(1)