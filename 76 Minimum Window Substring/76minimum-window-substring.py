class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        count_t = {}
        count_s = {}
        
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
            count_s[c] = 0
        
        required = len(count_t)
        formed = 0
        min_len = len(s) + 1
        res = [-1, -1]
        
        l = 0
        for r in range(len(s)):
            if s[r] in count_s:
                    count_s[s[r]] += 1
                    if count_s[s[r]] == count_t[s[r]]:
                        formed += 1
            while required == formed: 
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = [l, r]
                if s[l] in count_s:
                    count_s[s[l]] -= 1
                    if count_s[s[l]] < count_t[s[l]]:
                        formed -= 1
                l += 1
        l, r = res
        return s[l: r + 1]

# Time: O(n). n: len(s), m: len(t)
# Space: O(m) = O(26) = O(1)
"""
 "ef$axb$c$"
    l
            r
count_s = {$: 2, a: 1, b: 1, f: 1}
count_b = {$: 3, a: 1, b: 1, f: 0}

required = 4
formed = 3

min_len = 6
"""