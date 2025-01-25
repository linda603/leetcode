class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lists = list(s)

        for i in spaces:
            lists[i] = " " + lists[i]
        return "".join(lists)

# Time: O(n + m). n: len(s), m: len(spaces)
# Space: O(n)