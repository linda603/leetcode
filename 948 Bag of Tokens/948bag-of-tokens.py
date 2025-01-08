class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        scores = 0
        res = 0

        while l <= r:
            if power >= tokens[l]:
                scores += 1
                res = max(res, scores)
                power -= tokens[l]
                l += 1
            elif scores:
                scores -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return res

# Time: O(nlogn + n)
# Space: O(n)