class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open, close, curr):
            if open == close == n:
                res.append(curr)
                return
            if open < n:
                backtrack(open + 1, close, curr + "(")
            if close < open:
                backtrack(open, close + 1, curr + ")")
            return
        backtrack(0, 0, "")
        return res 

# Time: O(2^2n*(2n))
# Space: O(2n +2n) = O(n). 2n depth of backtrack, 2n curr "" space