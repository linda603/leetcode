class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit_to_c = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def dfs(i, curr):
            nonlocal res
            if i >= len(digits):
                res.append(curr)
                return
            for c in digit_to_c[digits[i]]:
                dfs(i + 1, curr + c)
            return
        dfs(0, "")
        return res

# Time: O(4^n)
# Space: O(n)