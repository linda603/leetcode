class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        string = ""

        for c, lock in zip(s, locked):
            if lock == "0":
                string += "*"
            else:
                string += c

        max_open = 0
        min_open = 0

        for c in string:
            if c == "(":
                max_open += 1
                min_open += 1
            elif c == ")":
                max_open -= 1
                min_open -= 1
            elif c == "*":
                max_open += 1
                min_open -= 1
            if max_open < 0:
                
                return False
            if min_open < 0:
                min_open = 0

        return True if not min_open else False

# Time: O(n)
# Space: O(1)