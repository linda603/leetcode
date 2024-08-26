class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_r = 0
        b_count_l = 0

        for c in s:
            a_count_r += 1 if c == "a" else 0
        
        res = len(s)
        for i, c in enumerate(s):
            a_count_r -= 1 if c == 'a' else 0
            res = min(res, a_count_r + b_count_l)
            b_count_l += 1 if c == 'b' else 0
        
        return res

#Time: O(n)
#Space: O(1)